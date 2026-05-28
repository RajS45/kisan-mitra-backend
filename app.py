from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "Kisan Mitra AI Backend API is running successfully!",
        "version": "1.0.0"
    }), 200