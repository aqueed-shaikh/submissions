#this is a file I wrote yesterday.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>This is the home page</h2>"

@app.route("/about")
def about():
    return "<b>This page was made by meeeeee!</b>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
