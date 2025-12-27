from flask import Flask, request, jsonify
from flask_cors import CORS
from db import users
from codeforces import get_codeforces_data
from codechef import get_codechef_data

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "CPulse Backend Running"

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json

    cf = get_codeforces_data(data["codeforces"])
    cc = get_codechef_data(data["codechef"])

    if not cf or not cc:
        return jsonify({"error": "Invalid Handles"}), 400

    user = {
        "name": data["name"],
        "codeforces": cf,
        "codechef": cc
    }

    users.insert_one(user)
    return jsonify({"message": "User added successfully"})

@app.route("/leaderboard")
def leaderboard():
    data = list(users.find({}, {"_id": 0}))
    data.sort(key=lambda x: x["codeforces"]["rating"], reverse=True)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
