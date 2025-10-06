# dashboard/traces_ui.py
import streamlit as st, os, json
st.title("Traces UI")
files = sorted([f for f in os.listdir("./Logs/Traces") if f.endswith(".json")], reverse=True) if os.path.exists("./Logs/Traces") else []
sel = st.selectbox("Trace", files)
if sel:
    with open(f"./Logs/Traces/{sel}") as f: st.json(json.load(f))
