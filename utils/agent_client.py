class AgentClient:
    def __init__(self):
        self.model = 'qwen2.5:72b-instruct-q3_k_m'
    def call_local(self, prompt):
        return f'Result for: {prompt}'
