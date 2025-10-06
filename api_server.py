from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json
import time

# --------------------------
# FastAPI app setup
# --------------------------
app = FastAPI(
    title="War AI API",
    version="1.0",
    description="Custom API with your logo and docs."
)

# --------------------------
# Track uptime
# --------------------------
start_time = time.time()

# --------------------------
# Directory paths
# --------------------------
BASE_DIR = Path(__file__).parent.resolve()
STATIC_DIR = BASE_DIR / "static"        # Your custom images/icons
SWARMS_DIR = BASE_DIR / "swarms"        # Agents folder
LOG_DIR = BASE_DIR / "data/logs"        # Logs
CONFIG_FILE = BASE_DIR / "config.json"  # Config file

# --------------------------
# Mount static files
# --------------------------
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --------------------------
# Root endpoint
# --------------------------
@app.get("/", tags=["System"])
async def root():
    img_file = STATIC_DIR / "custom_image.png"
    if img_file.exists():
        return FileResponse(img_file)
    return {
        "message": "War AI API running.",
        "docs": "Visit /docs for API reference",
        "endpoints": [
            "/health",
            "/api/status",
            "/api/config",
            "/api/logs",
            "/api/agents"
        ]
    }

# --------------------------
# Health check
# --------------------------
@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok"}

# --------------------------
# API status
# --------------------------
@app.get("/api/status", tags=["System"])
async def api_status():
    uptime_seconds = int(time.time() - start_time)
    return {
        "status": "running",
        "uptime_seconds": uptime_seconds,
        "active_agents": 0  # will be dynamic later
    }

# --------------------------
# Get logs
# --------------------------
@app.get("/api/logs", tags=["System"])
async def get_logs(limit: int = 10):
    if not LOG_DIR.exists():
        return {"logs": []}

    logs = []
    for file in sorted(LOG_DIR.glob("*.log"), reverse=True):
        with open(file, "r") as f:
            lines = f.readlines()
            logs.extend(lines[-limit:])
    
    return {"logs": logs[-limit:]}

# --------------------------
# Get config
# --------------------------
@app.get("/api/config", tags=["System"])
async def get_config():
    if not CONFIG_FILE.exists():
        raise HTTPException(status_code=404, detail="Config file not found")
    
    with open(CONFIG_FILE, "r") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Invalid JSON in config file")
    
    return {"config": config}

# --------------------------
# List agents
# --------------------------
@app.get("/api/agents", tags=["Agents"])
async def list_agents():
    if not SWARMS_DIR.exists():
        return {"agents": []}
    
    agents = [
        f.stem for f in SWARMS_DIR.glob("*.py")
        if f.is_file() and f.name != "__init__.py"
    ]
    return {"agents": agents}

# --------------------------
# Placeholder: run agent (to implement later)
# --------------------------
@app.post("/api/agents/run", tags=["Agents"])
async def run_agent(agent_name: str):
    agent_file = SWARMS_DIR / f"{agent_name}.py"
    if not agent_file.exists():
        raise HTTPException(status_code=404, detail=f"Agent '{agent_name}' not found")
    
    # Placeholder: logic to run agent goes here
    return {"message": f"Agent '{agent_name}' executed (placeholder)."}




