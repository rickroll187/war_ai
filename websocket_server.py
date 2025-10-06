# websocket_server.py
import asyncio, websockets, glob, os, json, time
SUBS=set()

async def notify():
    seen=set()
    while True:
        files=set(glob.glob("./Logs/**/*", recursive=True))
        new=files-seen
        if new:
            msg=json.dumps({"new": list(new)[:10]})
            for s in list(SUBS):
                try:
                    await s.send(msg)
                except:
                    SUBS.remove(s)
        seen=files
        await asyncio.sleep(5)

async def handler(ws, path):
    SUBS.add(ws)
    try:
        await ws.wait_closed()
    finally:
        if ws in SUBS: SUBS.remove(ws)

if __name__=="__main__":
    import websockets, asyncio
    start = websockets.serve(handler,"0.0.0.0",8765)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(start)
    loop.create_task(notify())
    loop.run_forever()
