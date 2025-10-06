# crypto_monitoring/watchlist.py
import json, os
FILE="./data/watchlist.json"
os.makedirs(os.path.dirname(FILE), exist_ok=True)
if not os.path.exists(FILE):
    with open(FILE,"w") as f: json.dump([],f)

def add(addr):
    with open(FILE,"r+") as f:
        lst = json.load(f)
        if addr not in lst: lst.append(addr)
        f.seek(0); f.truncate(); json.dump(lst,f)

def list_all():
    with open(FILE) as f: return json.load(f)
