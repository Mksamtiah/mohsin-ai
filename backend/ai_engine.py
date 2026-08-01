from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class AIEngine:
    def __init__(self):
        self.system_prompt = """
        You are Mohsin AI — a friendly, intelligent, and helpful assistant.
        You speak in a warm, clear, and professional tone.
        You help with coding, writing, analysis, reasoning, and everyday tasks.
        You remember previous parts of the conversation.
        You are polite, concise, and helpful.
        """
    
    def chat(self, messages):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
