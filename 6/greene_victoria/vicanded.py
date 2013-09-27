from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Edric!  How are you today?</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run()
