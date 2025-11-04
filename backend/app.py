from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/predict", methods=["POST","GET"])
def predict():
    # Stubbed response to simulate ML model
    return jsonify({"label": "Stop", "confidence": 0.95})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

