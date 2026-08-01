# Mohsin AI — Personal AI Assistant

A full-stack AI assistant with memory, built with FastAPI + Streamlit + OpenAI.

## Features
- 💬 Chat with memory
- 🧠 Persistent conversations
- 🔒 Private & secure
- 🌐 Deployed on Render.com

## Setup
1. Fork this repo
2. Add `OPENAI_API_KEY` in Render environment
3. Deploy!

## Local Development
```bash
pip install -r requirements.txt
cd backend && uvicorn app:app --reload
cd frontend && streamlit run streamlit_app.py
