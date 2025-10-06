# swarms/observability.py
import os, json, time, uuid
LOG_DIR = "./Logs/Traces"
os.makedirs(LOG_DIR, exist_ok=True)

class Trace:
    def __init__(self, agent, task):
        self.id = str(uuid.uuid4())
        self.agent = agent
        self.task = task
        self.start = time.time()
        self.events = []

    def log(self, name, data=None):
        self.events.append({"ts": time.time(), "name": name, "data": data or {}})

    def close(self, status="ok"):
        self.status = status
        self.duration = time.time() - self.start
        path = f"{LOG_DIR}/{self.id}.json"
        with open(path,"w") as f:
            json.dump(self.__dict__, f, default=str, indent=2)
        return path
