import concurrent.futures
import json
import os
import threading
import time
import urllib.error
import urllib.request

url = os.environ.get("TARGET_URL", "http://api")
rate = float(os.environ.get("REQUESTS_PER_SECOND", "4"))
slots = threading.BoundedSemaphore(16)

def request():
    start = time.monotonic()
    status = None
    error = None
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            response.read()
            status = response.status
    except urllib.error.HTTPError as exc:
        status, error = exc.code, str(exc)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        error = str(exc)
    finally:
        print(json.dumps({"timestamp": time.time(), "status": status, "latency_seconds": time.monotonic() - start, "error": error}), flush=True)
        slots.release()

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
    deadline = time.monotonic()
    while True:
        if slots.acquire(blocking=False):
            pool.submit(request)
        else:
            print(json.dumps({"timestamp": time.time(), "event": "load_generator_saturated"}), flush=True)
        deadline += 1 / rate
        time.sleep(max(0, deadline - time.monotonic()))
