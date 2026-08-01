import streamlit as st
import requests
import os

# Page config
st.set_page_config(
    page_title="Mohsin AI",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .stChatInput {
        border-radius: 20px;
    }
    .stButton button {
        border-radius: 20px;
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Mohsin AI — Your Personal Assistant")
st.caption("Powered by GPT-4o-mini")

# API endpoint - Render.com par automatic detect
API_URL = os.getenv("API_URL", "https://mohsin-ai.onrender.com")  # Deploy ke baad change

# Initialize session
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.session_id = None
        st.rerun()
    
    st.divider()
    st.caption("Made with ❤️ by Mohsin AI")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask Mohsin AI anything..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):
            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "session_id": st.session_state.session_id,
                        "message": prompt
                    },
                    timeout=60
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.session_id = data["session_id"]
                    reply = data["reply"]
                    st.write(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {str(e)}")
                st.info("Make sure the backend is running on Render.com")
