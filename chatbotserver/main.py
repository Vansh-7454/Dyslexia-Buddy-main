from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# OpenRouter API configuration
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"  # Replace with your actual API key

headers = {
    'Authorization': f"Bearer {API_KEY}",
    'Content-Type': 'application/json',
    'HTTP-Referer': 'https://team-x-amuhacks-4-0-ic2o.vercel.app/',  # Required by OpenRouter
    'X-Title': 'Dyslexia Helper Bot'   # Your app name
}

# Dyslexia-specific system prompt
SYSTEM_PROMPT = """
You are a friendly AI assistant helping people understand dyslexia. 
- Use simple, clear language with short sentences.
- Offer practical tips and emotional support.
- Highlight strengths of dyslexic individuals.
- Format responses with bullet points or numbered lists when helpful.
"""

@app.route("/ask", methods=['POST'])
def ask_ai():
    user_msg = request.json.get('message')

    data = {
        'model': 'deepseek-ai/deepseek-chat',  # Latest chat-optimized model
        'messages': [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': user_msg}
        ],
        'temperature': 0.3,  # Lower for more factual responses
        'max_tokens': 1000    # Enough for detailed but concise answers
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        response_json = response.json()
        answer = response_json["choices"][0]["message"]["content"]
        
        # Process answer for dyslexia-friendly formatting
        answer = answer.replace('\n\n', '\n')  # Simplify spacing
        
    except Exception as e:
        answer = f"Sorry, I encountered an error: {str(e)}. Please try again."

    return jsonify({
        'answer': answer,
        'status': 'success'
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)