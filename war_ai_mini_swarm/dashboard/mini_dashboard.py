import streamlit as st
import time

st.title("Mini Swarm Dashboard")
status_text = st.empty()

for i in range(10):
    status_text.text(f"Task progress: {i*10}%")
    time.sleep(0.5)

st.success("Mini Swarm tasks completed!")
