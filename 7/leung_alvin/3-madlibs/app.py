from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

blanks = {
    'NAMES': [],
    'PLACES': [],
    'NOUNS': [],
    'ADJS': [],
    'VERBS': [],
    'ADVS': []
}

@app.route("/")
def home():
    return "<h1>This is the home page</h1>"

@app.route("/madlibs")
def madlibs():
    return render_template("madlibs.html",place = "forest",name = "Mr. Z")

if __name__ == "__main__":
    app.debug=True
    app.run()
