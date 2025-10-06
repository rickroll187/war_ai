# cybersecurity/threat_detection.py
import os, json, time
LOG_DIR="./Logs/Detection"
os.makedirs(LOG_DIR, exist_ok=True)

def detect(event: dict):
    details = event.get("details","").lower()
    sev = "low"
    if any(k in details for k in ["ransom","modbus","unauthorized","exploit"]):
        sev = "high"
    out = {"ts": int(time.time()), "src": event.get("source"), "summary": event.get("summary"), "details": event.get("details"), "severity": sev}
    with open(f"{LOG_DIR}/alert_{int(time.time())}.json","w") as f: json.dump(out,f,indent=2)
    return out
