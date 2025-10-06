# dashboard/main_dashboard.py
import streamlit as st, glob, json, subprocess, os
st.title("WAR AI Dashboard")

if st.button("Run GitHub Triage"):
    subprocess.Popen(["python","swarms/github_triage.py"])

st.header("Swarm Results")
for p in sorted(glob.glob("./Logs/Swarm/*.json"), reverse=True)[:10]:
    with open(p) as f: st.json(json.load(f))

st.header("Traces")
for p in sorted(glob.glob("./Logs/Traces/*.json"), reverse=True)[:10]:
    with open(p) as f: st.json(json.load(f))
