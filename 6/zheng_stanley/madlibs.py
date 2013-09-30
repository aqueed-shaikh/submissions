#!/usr/bin/python
from flask import Flask
from flask import render_template
import random
app = Flask(__name__)


@app.route("/")
def home():	
	pv = ['crucified', 'died', 'cried', 'sighed' 'tried', 'pried', 'dried', 'lied']
	av = ['passionately', 'affectionately', 'deeply', 'dastardly', 'inappropriately']
	n = ['centurion', 'closet', 'livestock', 'son', 'uncle', 'car', 'dumpster', 'bear', 'dragon', 'bread']
	pn = ['pennies', 'mountains', 'sea cucumbers', 'angels', 'socks', 'bowls']


	return render_template("1.html", pv1 = random.choice(pv), 
					pv2 = random.choice(pv), 
					av1 = random.choice(av), 
					n1 = random.choice(n), 
					n2 = random.choice(n), 
					n3 = random.choice(n), 
					n4 = random.choice(n), 
					n5 = random.choice(n),
					pn1 = random.choice(pn), 
					pn2 = random.choice(pn), 
					pn3 = random.choice(pn)
				)


if __name__ == "__main__":
	app.debug = True
	app.run();

# Worked with Raymond Lam Period 6
