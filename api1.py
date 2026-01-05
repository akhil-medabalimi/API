from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API running"})

@app.route("/user/<int:user_id>")
def get_user(user_id):
    return jsonify({
        "user_id": user_id,
        "name": "Alice"
    })

if __name__ == "__main__":
    app.run(debug=True)
