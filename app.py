import streamlit as st
from agent import DroneAgent
import json

st.title("🛩️ Skylark Drones AI Coordinator")
st.markdown("**Test queries:** *available pilots Bangalore*, *match PRJ001*, *drones thermal*, *assign P001 PRJ001*")

agent = DroneAgent()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# New message
if prompt := st.chat_input("Ask about pilots, drones, assignments..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = agent.chat(prompt)
        # Pretty print tables
        if isinstance(response, list):
            st.json(response)
        else:
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": str(response)})
