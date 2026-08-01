from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine import AIEngine
from memory import Memory
import uuid
import os

app = FastAPI(title="Mohsin AI Backend")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production mein specific domains daalein
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai = AIEngine()
memory = Memory()

class ChatRequest(BaseModel):
    session_id: str | None = None
    message: str

class ChatResponse(BaseModel):
    session_id: str
    reply: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not req.session_id:
        req.session_id = str(uuid.uuid4())
    
    # Get history
    history = memory.get_history(req.session_id)
    
    # Build messages
    messages = [{"role": "system", "content": ai.system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": req.message})
    
    # Get AI reply
    reply = ai.chat(messages)
    
    # Store in memory
    memory.add_message(req.session_id, "user", req.message)
    memory.add_message(req.session_id, "assistant", reply)
    
    return ChatResponse(session_id=req.session_id, reply=reply)

@app.get("/")
def root():
    return {"message": "Mohsin AI is running!", "status": "active"}

@app.get("/health")
def health():
    return {"status": "healthy"}
