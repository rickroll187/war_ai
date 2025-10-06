# api_server.py
from fastapi import FastAPI, HTTPException
import glob, json, os, subprocess
from pydantic import BaseModel

app = FastAPI(title="WAR AI API")

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/swarm/triage")
def run_triage(repo: str):
    # Run the local swarm script (blocking)
    r = subprocess.run(["python","swarms/github_triage.py",repo], capture_output=True, text=True)
    if r.returncode != 0:
        raise HTTPException(status_code=500, detail=r.stderr)
    return {"status":"started","output": r.stdout}

@app.get("/logs/{kind}")
def list_logs(kind: str):
    p = f"./Logs/{kind}"
    if not os.path.exists(p): return {"files":[]}
    files = sorted([os.path.basename(x) for x in glob.glob(p + "/*.json")], reverse=True)[:50]
    return {"files": files}
