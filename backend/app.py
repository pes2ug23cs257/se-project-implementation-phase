from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
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
