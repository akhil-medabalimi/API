from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running"

@app.route("/user/<int:user_id>")
def get_user(user_id):
    return {"user_id": user_id,
            "password": 1234} 

if __name__ == "__main__":
    app.run(debug=True)
