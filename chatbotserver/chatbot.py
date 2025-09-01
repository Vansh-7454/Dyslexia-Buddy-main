from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
SYSTEM_PROMPT = """
You are a friendly AI assistant helping people understand dyslexia. 
- Use simple, clear language with short sentences.
- Offer practical tips and emotional support.
- Highlight strengths of dyslexic individuals.
- Format responses with bullet points or numbered lists when helpful.
"""
# Configure Groq client
client = Groq(
    api_key="YOUR_API_KEY",
)

# Define input model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat_completion(request: ChatRequest):
    try:
        # Process the input message using Groq API
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': request.message}
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Collect the streamed response
        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""
        print("Response: ",response)
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

