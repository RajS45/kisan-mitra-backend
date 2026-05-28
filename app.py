@app.route("/", methods=["GET"])
def home():
    return flask.jsonify({
        "status": "online",
        "message": "Kisan Mitra AI Backend API is running successfully!",
        "version": "1.0.0"
    }), 200