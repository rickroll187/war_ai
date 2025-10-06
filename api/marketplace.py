# api/marketplace.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os, asyncio
from solana.rpc.async_api import AsyncClient

app = FastAPI(title="Marketplace")
SOLANA_RPC = os.getenv("SOLANA_RPC", "https://api.devnet.solana.com")
MERCHANT_ADDRESS = os.getenv("MARKET_RECEIVER_PUBKEY", "")

class PurchaseRequest(BaseModel):
    agent_id: str
    buyer_pubkey: str
    tx_signature: str

@app.get("/agents")
def list_agents():
    return [{"id":"phi3-mini-amd","price_sol":0.01,"desc":"Reasoning head"}]

@app.post("/purchase/verify")
async def verify(req: PurchaseRequest):
    async with AsyncClient(SOLANA_RPC) as client:
        resp = await client.get_transaction(req.tx_signature)
        if not resp.value:
            raise HTTPException(400,"tx not found")
        # crude check: ensure signature exists and status ok
        meta = resp.value.meta
        if not meta or meta.err:
            raise HTTPException(400,"tx failed")
        # In production inspect transfer instructions to ensure to=MERCHANT_ADDRESS
    return {"verified": True, "agent_id": req.agent_id}
