from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    """Returns the API status."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the dictionary."""
    # Check if request is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    
    # Check if username is provided
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Check if user already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user and return success
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
