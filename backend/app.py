"""Flask backend for traffic sign recognition mock API."""
import os
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import CORS # <-- Make sure this is installed (pip install flask-cors)

# --- 1. App Initialization ---
app = Flask(__name__)
CORS(app) 
CORS(app) # <-- This one line handles all CORS and OPTIONS requests

# --- 2. Health Check Route ---
@app.route('/')
def home():
    """Health-check route to verify the backend is running."""
    return "✅ Backend is running fine!"

# --- 3. Prediction Route (US-021) ---
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

    # --- Day 6 (US-021) Logic ---
    # This list makes your demo match the project title.
    labels = [
        "Stop Sign", 
        "Speed Limit 40", 
        "Speed Limit 60",
        "No Entry", 
        "Yield", 
        "Turn Left", 
        "Pedestrian Crossing"
    ]
    
    result = {
        "label": random.choice(labels),
        "confidence": round(random.uniform(0.85, 0.99), 2)
    }
    # --- End of logic ---

    return jsonify(result), 200

# --- 4. Run the App ---
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
