import json
import os
import ssl
import time
import urllib.error
import urllib.request
from pathlib import Path

account = Path("/var/run/secrets/kubernetes.io/serviceaccount")
namespace = account.joinpath("namespace").read_text().strip()
token = account.joinpath("token").read_text().strip()
context = ssl.create_default_context(cafile=str(account / "ca.crt"))
host = os.environ["KUBERNETES_SERVICE_HOST"]
if ":" in host:
    host = "[" + host + "]"
base = "https://" + host + ":" + os.environ["KUBERNETES_SERVICE_PORT_HTTPS"]
path = "/api/v1/namespaces/" + namespace + "/configmaps"
while True:
    for action, suffix in (("get", "/settings"), ("list", "")):
        request = urllib.request.Request(base + path + suffix, headers={"Authorization": "Bearer " + token})
        try:
            with urllib.request.urlopen(request, context=context, timeout=5) as response:
                body = json.load(response)
                print(json.dumps({"action": action, "status": response.status, "reconciled": action == "list", "timestamp": time.time()}), flush=True)
        except urllib.error.HTTPError as error:
            print(json.dumps({"action": action, "status": error.code, "error": error.read().decode(), "timestamp": time.time()}), flush=True)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            print(json.dumps({"action": action, "error": str(error), "timestamp": time.time()}), flush=True)
    time.sleep(5)
