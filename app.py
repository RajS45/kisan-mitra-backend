import os
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    # Render assigns a dynamic port via environment variables. Fallback to 5000 only for local testing.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)