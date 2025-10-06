# utils/agent_client.py
import os, time, threading, requests
from typing import Optional

"""
Agent client wrapper.
- call_local: POST to local model server (expect JSON {response: str})
- call_xai: calls cloud xAI endpoint with quota enforcement
"""

XAI_API_KEY = os.getenv("XAI_API_KEY", "")
XAI_ENDPOINT = os.getenv("XAI_ENDPOINT", "https://api.x.ai/v1/chat/completions")
LOCAL_MODEL_URL = os.getenv("LOCAL_MODEL_URL", "http://localhost:11434/api/generate")

MAX_REQ_PER_MIN = int(os.getenv("MAX_REQ_PER_MIN", "100"))
MAX_TOKENS_PER_MONTH = int(os.getenv("MAX_TOKENS_PER_MONTH", "100000"))

class TokenBucket:
    def __init__(self, rate_per_min: int):
        self.rate = rate_per_min
        self.tokens = rate_per_min
        self.lock = threading.Lock()
        self.last = time.time()

    def consume(self, n=1):
        with self.lock:
            now = time.time()
            elapsed = now - self.last
            refill = int(elapsed * (self.rate / 60.0))
            if refill > 0:
                self.tokens = min(self.rate, self.tokens + refill)
                self.last = now
            if self.tokens < n:
                wait = (n - self.tokens) * (60.0 / self.rate)
                time.sleep(wait)
                self.tokens = self.rate
                self.last = time.time()
            self.tokens -= n

class AgentClient:
    def __init__(self):
        self.bucket = TokenBucket(MAX_REQ_PER_MIN)
        self.monthly_tokens = 0
        self.lock = threading.Lock()

    def _count_tokens(self, text: str) -> int:
        # crude token estimation (words)
        return max(1, len(text.split()))

    def call_local(self, prompt: str, model: str="phi3-mini-amd", timeout: int=60) -> str:
        try:
            payload = {"model": model, "prompt": prompt}
            resp = requests.post(LOCAL_MODEL_URL, json=payload, timeout=timeout)
            resp.raise_for_status()
            data = resp.json()
            out = data.get("response") or data.get("output") or data.get("text") or ""
            # record tokens
            tok = self._count_tokens(prompt + out)
            with self.lock:
                self.monthly_tokens += tok
            return out
        except Exception as e:
            raise RuntimeError(f"Local model call failed: {e}")

    def call_xai(self, prompt: str, model: str="gpt-xai", timeout: int=60) -> str:
        self.bucket.consume(1)
        tok_est = self._count_tokens(prompt)
        with self.lock:
            if self.monthly_tokens + tok_est > MAX_TOKENS_PER_MONTH:
                raise RuntimeError("xAI monthly token limit exceeded")
        headers = {"Authorization": f"Bearer {XAI_API_KEY}"} if XAI_API_KEY else {}
        payload = {"model": model, "messages": [{"role":"user","content": prompt}]}
        resp = requests.post(XAI_ENDPOINT, headers=headers, json=payload, timeout=timeout)
        resp.raise_for_status()
        j = resp.json()
        # parse common shapes
        text = ""
        if isinstance(j.get("choices"), list) and j["choices"]:
            text = j["choices"][0].get("message", {}).get("content", "")
        text = text or j.get("output") or j.get("response_text", "")
        tok_used = self._count_tokens(prompt + text)
        with self.lock:
            self.monthly_tokens += tok_used
        return text

# export client
agent_client = AgentClient()
