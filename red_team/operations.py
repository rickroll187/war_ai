# red_team/operations.py
from .authorization import allowed

def run_nmap(target):
    if not allowed(): raise RuntimeError("Red team disabled")
    # sandboxed: require manual execution; here we return command to run in sandbox
    return {"cmd": f"docker run --rm --network host instrument/nmap {target}"}
