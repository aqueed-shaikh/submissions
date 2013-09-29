#! /usr/bin/env python
# Team members:
# Ben Kurtovic and Jing Lin

import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    words = {
        "P1": random.choice(["Brian", "Ben", "Jing"]),
        "N0": random.choice(["hill", "country"]),
        "P2": random.choice(["Seven", "Six", "Four", "Roger"]),
        "V1": random.choice(["kick", "eat", "step on", "laugh at", "sneeze on", "chase"]),
        "N1": random.choice(["trees", "redbull", "Snicker bars", "chicken wings", "Mac keyboards"]),
        "V2": random.choice(["prayed to", "rubbed", "washed", "touched", "sung at"]),
        "N2": random.choice(["cloud", "mountain", "chair", "bacon"]),
        "N3": random.choice(["cheddar cheese", "king", "waffle", "peanut butter", "jelly"]),
        "N4": random.choice(["people", "flowers", "grass", "water", "Mitsubishi"]),
        "N5": random.choice(["Sharknadoes", "whole-wheat bread", "apples", "frying pans"]),
        "V3": random.choice(["steal", "devour", "jump on", "cry on", "lick"]),
        "N6": random.choice(["lollipops", "honey", "bears", "frogs", "pigeons"])
    }
    return render_template("madlibs.html", d=words)

if __name__ == "__main__":
    app.run(debug=True)
