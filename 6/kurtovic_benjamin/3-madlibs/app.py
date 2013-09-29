#! /usr/bin/env python
# Team members:
# Ben Kurtovic and Jing Lin

import random
from flask import Flask, render_template

app = Flask(__name__)

words = {
    "P1": ["Brian", "Ben", "Jing"],
    "N0": ["hill", "country"],
    "P2": ["Seven", "Six", "Four", "Roger"],
    "V1": ["kick", "eat", "step on", "laugh at", "sneeze on", "chase"],
    "N1": ["trees", "redbull", "Snicker bars", "chicken wings", "Mac keyboards"],
    "V2": ["prayed to", "rubbed", "washed", "touched", "sung at"],
    "N2": ["cloud", "mountain", "chair", "bacon"],
    "N3": ["cheddar cheese", "king", "waffle", "peanut butter", "jelly"],
    "N4": ["people", "flowers", "grass", "water", "Mitsubishi"],
    "N5": ["Sharknadoes", "whole-wheat bread", "apples", "frying pans"],
    "V3": ["steal", "devour", "jump on", "cry on", "lick"],
    "N6": ["lollipops", "honey", "bears", "frogs", "pigeons"]
}

@app.route("/")
def home():
    story = {key: random.choice(words[key]) for key in words}
    return render_template("madlibs.html", d=story)

if __name__ == "__main__":
    app.run(debug=True)
