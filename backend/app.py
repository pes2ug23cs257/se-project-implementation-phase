"""Flask backend for traffic sign recognition mock API."""
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/predict", methods=["POST","GET"])
def predict():
    # Stubbed response to simulate ML model
    return jsonify({"label": "Stop", "confidence": 0.95})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, jsonify, request, make_response
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """Health-check route to verify the backend is running."""
    return "✅ Backend is running fine!"
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/predict", methods=["POST", "OPTIONS"])  # Add OPTIONS method
def predict():
    # Handle preflight request
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response
    
    # Get file from request
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    # Save the uploaded file temporarily
    filepath = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload and return a random traffic sign prediction."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    uploaded_file = request.files['file']
    # 🧠 mock prediction
    return jsonify({
        'label': 'Stop Sign',
        'confidence': 0.92
    })

if __name__ == '__main__':
    app.run(debug=True)
