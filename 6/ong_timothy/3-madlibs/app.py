#Team: Timothy Ong and Jason Zhen

from flask import Flask
from flask import render_template
from random import randrange as rr

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

bank = {
    "name"  : ['Sam', 'Brian', 'Anthony', 'Tommy', 'Johnson', 'William', 'Peyton Manning', 'Mike Vick'],
    "v"     : ['troll', 'smacked', 'throw',  'talk', 'punch', 'fly', 'jump'],
    "adj"   : ['stupid', 'sleepy', 'bored', 'genius', 'great', 'sad', 'happy', 'cocky'],
    "adv"   : ['skillfully', 'stupidly', 'quickly', 'slowly', 'quietly'],
    "n"     : ['hammer', 'textbook', 'sledgehammer', ' marker', 'pipecleaner', 'Ducky tie', 'dagger', 'dog'],
    "pl"    : ['5th floor boys bathroom', 'London', 'Trampa', 'Mumbai', 'Canaderp', 'Chicago']
}

@app.route("/madlibs")
def madlibs():
    return render_template(
        "madlibs.html", 
        name1 = bank["name"][rr(0,len(bank["name"]))],
        name2 = bank["name"][rr(0,len(bank["name"]))],
        name3 = bank["name"][rr(0,len(bank["name"]))],
        v1    = bank["v"]   [rr(0,len(bank["v"]))],
        noun1 = bank["n"]   [rr(0,len(bank["n"]))],
        adv1  = bank['adv'] [rr(0,len(bank['adv']))],
        pl1   = bank['pl']  [rr(0,len(bank['pl']))],
        pl2   = bank['pl']  [rr(0,len(bank['pl']))],
        adj1  = bank['adj'] [rr(0,len(bank['adj']))],
        adj2  = bank['adj'] [rr(0,len(bank['adj']))],
        adj3  = bank['adj'] [rr(0,len(bank['adj']))],
        adj4  = bank['adj'] [rr(0,len(bank['adj']))],
        n1    = bank['n']   [rr(0,len(bank['n']))]
        )


if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 9001)
