from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

bank = {
    "NAMES"  : ['Sam', 'Brian', 'Anthony', 'Tommy', 'Johnson', 'William', 'Peyton Manning', 'Mike Vick'],
    "VERBS"  : ['trolled', 'smacked', 'smacked', 'threw', 'pants\'d', 'talked', 'punched'],
    "ADJS"   : ['stupid', 'sleepy', 'bored', 'genius', 'great', 'sad', 'happy', 'cocky'],
    "ADVS"   : ['skillfully', 'stupidly', 'quickly', 'slowly', 'quietly'],
    "NOUNS"  : ['hammer', 'textbook', 'sledgehammer', ' marker', 'pipecleaner', 'Ducky tie', 'dagger', 'dog'],
    "PLACES" : ['5th floor boys bathroom', 'London', 'Trampa', 'Mumbai', 'Canaderp', 'Chicago']
}

@app.route("/madlibs")
def madlibs():
    return render_template("madlibs.html", 
                           name1 = bank["NAMES"][random.randrange(0,len(bank["NAMES"]))],
                           verb1 = bank["VERBS"][random.randrange(0,len(bank["VERBS"]))],
                           noun1 = bank["NOUNS"][random.randrange(0,len(bank["NOUNS"]))]
)


if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 9001)
