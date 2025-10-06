# swarms/github_triage.py
import os, sys, time, json, requests
from config.config import Config

OUT_DIR = "./Logs/Swarm"
os.makedirs(OUT_DIR, exist_ok=True)

def fetch_issues(repo, token=None):
    headers = {"Authorization": f"token {token}"} if token else {}
    r = requests.get(f"https://api.github.com/repos/{repo}/issues", headers=headers, params={"state":"open","per_page":30}, timeout=20)
    r.raise_for_status()
    return r.json()

def analyze_text(title, body):
    text = (title + "\n" + (body or ""))[:5000].lower()
    score = 0
    for k,v in [("security",10),("critical",9),("bug",4),("crash",7)]:
        if k in text: score += v
    pr = "low"
    if score>=9: pr="high"
    elif score>=4: pr="medium"
    return {"priority":pr,"score":score}

def run(repo="fahamgeer177/Triage.AI"):
    issues = fetch_issues(repo, token=Config.GITHUB_TOKEN)
    results=[]
    for i in issues:
        a = analyze_text(i.get("title",""), i.get("body",""))
        results.append({"number":i.get("number"),"title":i.get("title"),"priority":a})
    out = {"repo":repo,"ts":int(time.time()),"results":results}
    with open(f"{OUT_DIR}/triage_{int(time.time())}.json","w") as f:
        json.dump(out,f,indent=2)
    return out

if __name__=="__main__":
    repo = sys.argv[1] if len(sys.argv)>1 else "fahamgeer177/Triage.AI"
    print(run(repo))
