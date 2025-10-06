import os
import zipfile

# Base directory for the ZIP structure
base_dir = "war_ai_mini_swarm"
os.makedirs(base_dir, exist_ok=True)

# Define files and their functional content
files = {
    "core/main_swarm.py": """
import multiprocessing
from swarms.mini_swarm import run_tasks
from utils.agent_client import AgentClient

def main():
    print("[Mini Swarm] Starting Boss-Worker orchestrator...")
    agent_client = AgentClient(model='phi3-mini-amd')
    processes = []
    for task_name in ['github_triage', 'research', 'crypto_monitor']:
        p = multiprocessing.Process(target=run_tasks, args=(task_name, agent_client))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print("[Mini Swarm] All tasks completed.")

if __name__ == "__main__":
    main()
""",
    "utils/agent_client.py": """
import time

class AgentClient:
    def __init__(self, model='phi3-mini-amd'):
        self.model = model

    def run(self, task_name, payload=None):
        print(f"[AgentClient] Running task '{task_name}' on model {self.model}...")
        time.sleep(1)
        return f"Result of {task_name}"
""",
    "swarms/mini_swarm.py": """
def run_tasks(task_name, agent_client):
    print(f"[Mini Swarm] Executing {task_name} task...")
    result = agent_client.run(task_name)
    print(f"[Mini Swarm] {task_name} result: {result}")
""",
    "dashboard/mini_dashboard.py": """
import streamlit as st
import time

st.title("Mini Swarm Dashboard")
status_text = st.empty()

for i in range(10):
    status_text.text(f"Task progress: {i*10}%")
    time.sleep(0.5)

st.success("Mini Swarm tasks completed!")
""",
    "blockchain/mock_blockchain.py": """
def log_threat(threat_name, severity=1):
    print(f"[Blockchain] Logging threat '{threat_name}' with severity {severity} (mock).")
    return True
""",
    "logs/mini_swarm.log": ""  # Empty file, logs can be written by tasks
}

# Create directories and files
for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content.strip() + "\n")

# Generate ZIP
zip_path = "war_ai_mini_swarm.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, filenames in os.walk(base_dir):
        for file in filenames:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, base_dir))

print(f"✅ Mini swarm ZIP generated: {zip_path}")
