from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"

# Dyslexia-specific system prompt
SYSTEM_PROMPT = """
You are a friendly AI assistant helping people understand dyslexia. 
- Use simple, clear language with short sentences.
- Offer practical tips and emotional support.
- Highlight strengths of dyslexic individuals.
- Format responses with bullet points or numbered lists when helpful.
"""

headers = {
    'Authorization': f"Bearer {API_KEY}",
    'Content-Type': 'application/json'
}

@app.route("/ask", methods=['POST'])
def askai():
    user_msg = request.json.get('message')
    print("Message: ",user_msg)

    data = {
        'model': 'deepseek/deepseek-r1:free',
        'messages': [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': user_msg}
        ],
        'temperature': 0.7
    }

    res = requests.post(URL, headers=headers, json=data)

    try:
        response_json = res.json()  # Convert response to JSON
        # Check if "choices" key exists in response
        if "choices" in response_json:
            answer = response_json["choices"][0]["message"]["content"]
        else:
            answer = "Error: Unexpected response format"

    except Exception as e:
        answer = f"Error processing response: {str(e)}"

    print("answer: ",type(answer))
    return {'message': answer}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
