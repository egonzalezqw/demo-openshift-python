from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 8080))

@app.route("/")
def home():
    return "🚀 Hola OpenShift! App Python desplegada correctamente."

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "time": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
