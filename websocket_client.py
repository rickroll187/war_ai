# websocket_client.py
import asyncio, websockets

async def listen():
    async with websockets.connect("ws://localhost:8765") as ws:
        async for msg in ws:
            print("MSG", msg)

if __name__=="__main__":
    asyncio.run(listen())
