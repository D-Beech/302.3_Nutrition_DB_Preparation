from flask import Flask, request, jsonify
from llm_service import LLMService

app = Flask(__name__)
llm_service = LLMService()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/log_input', methods=['POST'])
def log_input():
    try:
        data = request.get_json()
        user_input = data.get('input', '')
        
        if not user_input:
            return jsonify({'error': 'No input provided'}), 400
        
        response = llm_service.chat_completion(user_input)
        
        return jsonify({
            'user_input': user_input,
            'llm_response': response
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
