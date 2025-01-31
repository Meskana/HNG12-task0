from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/", methods=["GET"])
def public_api():
    """Returns email, current time in ISO 8601 format, and GitHub repo URL."""
    now = datetime.now().replace()
    current_time = now.isoformat()[:-3] + "Z"
    response_data = {
        "email":"marcelinusilonuba21@gmail.com",
        "github_url":"https://github.com/Meskana/HNG12-task0",
        "current_datetime":current_time
    }
    return jsonify(response_data), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
