from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

words= {'propernoun' : [Steve, Jasper, Roger, Ben, Jing, Jason, Marlena, Jane, Pascu],
	'noun' : "laptop, clock, chair, gun, clock, toilet",
	'verb' : "runs, shoots, kills, steals, saves, naps",
	'adjective' : "fabulous, harmonious, wordy, slow, fast, dumb",
	'place' : "McDonalds, Sydney, Burger King, the Sahara, Google Headquarters"
	}

l = [words['propernoun'][random.randrange(0, len(words.propernoun))],
	words['noun'][random.randrange(0, len(words.verb))],
	words['verb'][random.randrange(0, len(words.place))],
	words['adjective'][random.randrange(0, len(words.adjective))],
	words['noun'][random.randrange(0, len(words.noun))]]


@app.route("/")
def mad():
    return render_template(template.html, l=l);

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=5005)
