import time

class AgentClient:
    def __init__(self, model='phi3-mini-amd'):
        self.model = model

    def run(self, task_name, payload=None):
        print(f"[AgentClient] Running task '{task_name}' on model {self.model}...")
        time.sleep(1)
        return f"Result of {task_name}"
