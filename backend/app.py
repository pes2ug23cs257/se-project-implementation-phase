"""Flask backend for traffic sign recognition mock API."""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """Health-check route to verify the backend is running."""
    return "✅ Backend is running fine!"

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
