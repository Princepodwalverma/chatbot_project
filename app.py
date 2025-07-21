from flask import Flask, render_template, request
from chatbot import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_input = request.args.get("msg")
    bot_response = get_bot_response(user_input)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
