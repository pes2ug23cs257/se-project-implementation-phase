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

    # Placeholder prediction
    result = {
        "label": "Speed Limit 60",
        "confidence": 0.92
    }

    # Optional cleanup
    os.remove(filepath)

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)