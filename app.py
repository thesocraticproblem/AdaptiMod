from flask import Flask, request, jsonify
from flask_cors import CORS  # For cross-origin requests (optional)
import random  # For placeholder Q(A) score

app = Flask(__name__)
CORS(app)  # Enable CORS if needed

@app.route('/qa', methods=['POST'])
def calculate_qa():
    # Get text input from request
    data = request.json
    text = data.get('text', '')
    
    # Placeholder Q(A) logic (replace with actual GFU calculations later)
    qa_score = random.uniform(0.0, 1.0)  # Random score between 0 and 1
    
    return jsonify({
        'text': text,
        'qa_score': qa_score,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True)  # Run locally