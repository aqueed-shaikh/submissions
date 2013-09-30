from flask import Flask
from flask import render_template

import random


app = Flask(__name__)

@app.route("/madlib")
def madlib():
    names = ["James", "Alex", "Bill", "Joe", "Daniel", "John"]
    verbs = ["ate", "found", "saw", "smelled", "heard"]
    nouns = ["fish", "rock"]
    places = ["park", "woods", "street"]
    adjs = ["Surprised", "Upset", "Angry", "Annoyed"]
    d={'name': random.choice(names),
       'friend': random.choice(names),
       'verb': random.choice(verbs),
       'place': random.choice(places),
       'noun': random.choice(nouns),
       'adj': random.choice(adjs)
       }
    
    return render_template("madlib.html",d=d);

@app.route("/")
def home():
    return render_template("index.html");

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5006)
