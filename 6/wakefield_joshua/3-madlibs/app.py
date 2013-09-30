#! /usr/bin/env python
# Roger Li
# Joshua Wakefield

import random
from flask import Flask, render_template

app = Flask(__name__)

words = {
	"F" : ["Skirmish", "Blitzkreig", "Clash"],
    "W" : ["Sunny", "Rainy", "Stormy", "Cloudy"],
	"V1": ["killed", "eaten", "kicked", "poked", "tickled"],
	"M1": ["dragon", "beast", "lion", "bear"],
	"L" : ["castle", "fort", "shack", "mudhouse"],
	"V2": ["revive", "punch", "attack", "defend"],
	"V3": ["approached", "looked at", "licked", "spat on"],
	"A1": ["wimpy", "puny", "weak", "tiny"],
	"N1": ["toilet", "pillow", "baseball bat", "axe"],
	"V4": ["swung", "threw", "launched", "flung"],
	"BW": ["pool", "vat", "lava", "boiling pot"],
	"N2": ["alligators", "pirahnas", "sharks"],
	"V5": ["ran", "flew", "glided", "jogged"],
	"L2": ["room", "quarters", "couch"],
	"V6": ["**** *******", "********", "****** **", "***** *****"]
}

@app.route("/")
def home():
    keys = {key: random.choice(words[key]) for key in words}
    return render_template("madlibs.html", d=keys)

if __name__ == "__main__":
    app.run(debug=True)
