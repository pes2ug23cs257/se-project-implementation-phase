"""Flask backend for traffic sign recognition mock API."""
import os
import random
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    """Health-check route to verify the backend is running."""
    return "✅ Backend is running fine!"

@app.route("/predict", methods=["POST"])
def predict():
    """
    Handles image upload and returns a random, realistic
    mock traffic sign prediction.
    """
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    labels = [
        "Stop Sign", "Speed Limit 40", "Speed Limit 60",
        "No Entry", "Yield", "Turn Left", "Pedestrian Crossing"
    ]

    result = {
        "label": random.choice(labels),
        "confidence": round(random.uniform(0.85, 0.99), 2)
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
