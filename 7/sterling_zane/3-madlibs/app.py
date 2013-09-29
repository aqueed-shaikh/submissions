from flask import Flask
from flask import render_template
import random

app = Flask("Buzzard")

properNouns = ["Zane", "Sebastian"]
adjectives = ["colored", "yellow"]
places = ["St Marks Square"]
nouns = ["potato", "elephant"]
verbs = ["bungee jumping", "flying"]


@app.route("/")
def home():
	return render_template("index.html", properNouns=properNouns,
						   nouns=nouns, verbs=verbs, adjectives=adjectives,
						   random=random, places=places)

if __name__ == "__main__":
	app.run(debug = True)
