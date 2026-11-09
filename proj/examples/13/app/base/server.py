from pathlib import Path
Path("/data/baseline.txt").write_text("disposable test data\n")
import hashlib
import json
import os
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

mode = os.environ.get("APP_MODE", "production")
if mode not in {"production", "development"}:
    print(json.dumps({"error": "invalid APP_MODE", "value": mode}), flush=True)
    raise SystemExit(1)
startup = int(os.environ.get("STARTUP_SECONDS", "0"))
print(json.dumps({"event": "initializing", "startup_seconds": startup}), flush=True)
time.sleep(startup)
blocks = []

def allocate():
    amount = int(os.environ.get("ALLOCATE_MIB", "0"))
    if not amount:
        return
    time.sleep(10)
    for offset in range(0, amount, 8):
        blocks.append(bytearray(min(8, amount - offset) * 1024 * 1024))
        print(json.dumps({"event": "allocation", "retained_mib": min(offset + 8, amount)}), flush=True)
        time.sleep(1)
    print(json.dumps({"event": "working_set_ready", "retained_mib": amount}), flush=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, body = 200, b"ok\n"
        if self.path not in {"/", "/ready", "/live"}:
            status, body = 404, b"unknown path\n"
        elif self.path == "/":
            iterations = int(os.environ.get("CPU_ITERATIONS", "0"))
            if iterations:
                hashlib.pbkdf2_hmac("sha256", b"request", b"fixed-salt", iterations)
            dependency = os.environ.get("DEPENDENCY_URL")
            if dependency:
                try:
                    with urllib.request.urlopen(dependency, timeout=2) as response:
                        body = response.read()
                except (urllib.error.URLError, TimeoutError, OSError) as error:
                    status, body = 502, b"dependency unavailable\n"
                    print(json.dumps({"event": "dependency_error", "url": dependency, "error": str(error)}), flush=True)
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

threading.Thread(target=allocate, daemon=True).start()
port = int(os.environ.get("PORT", "8080"))
print(json.dumps({"event": "listening", "port": port}), flush=True)
ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
