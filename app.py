from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Production Configuration
#app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False  # Optimized for performance

@app.route("/api/public", methods=["GET"])
def public_api():
    """Returns email, current time in ISO 8601 format, and GitHub repo URL."""
    response_data = {
        "email": "marcelinusilonuba21@gmail.com",
        "current_time": datetime.now(pytz.utc).isoformat(),
        "github_repo": "https://github.com/Meskana/HNG12-task0.git"
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
