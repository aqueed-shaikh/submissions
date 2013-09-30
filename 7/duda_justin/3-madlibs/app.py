from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route("/madlib")
def madlib():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] 
    names = ["James", "Alex", "Bill", "Joe", "Daniel", "John"]
    verbs = ["ate", "found", "saw", "smelled", "heard"]
    nouns = ["fish", "rock", "cake", "earing", "turtle", "stone"]
    places = ["park", "woods", "street"]
    adjs = ["Surprised", "Upset", "Angry", "Annoyed"]
    d={'name': random.choice(names),
       'friend': random.choice(names),
       'verb': random.choice(verbs),
       'place': random.choice(places),
       'noun': random.choice(nouns),
       'adj': random.choice(adjs)
       }
s = "It was a %(days)s, and %(names)s was at home. He %(verbs)s a %(nouns)s in the %(places)s. He was very %(adjs)s and %(d)s. " 
    
    return render_template("madlib.html",s = s%(d));

@app.route("/")
def home():
    return "<h1> JUSTIN AND CHRISTINE ROCK THE WORLD!!! </hl>"
    return render_template("index.html");


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5006)


@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"
