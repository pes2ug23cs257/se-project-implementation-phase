"""Flask backend for traffic sign recognition mock API."""
import os
import random  # <-- ADDED for Day 6 random predictions
from flask import Flask, jsonify, request, make_response

# --- 1. App Initialization (Kept your single app definition) ---
app = Flask(__name__)
CORS(app)
# --- 2. CORS Headers (Kept your manual @after_request headers) ---
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# --- 3. Health Check Route (Kept your home route) ---
@app.route('/')
def home():
    """Health-check route to verify the backend is running."""
    return "✅ Backend is running fine!"

# --- 4. Prediction Route (Combined your functions + Added Day 6 logic) ---





@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    """
    Handles image upload and returns a random, realistic
    mock traffic sign prediction (Implements US-021).
    """
    
    # Handle preflight CORS request
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

    # Handle POST request
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    # --- (SLIGHT CHANGE) Day 6 (US-021) Logic ---
    # We don't need to save the file, just return the mock.
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
    # --- End of change ---

    return jsonify(result), 200

# --- 5. Run the App (Kept your final run command) ---
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
