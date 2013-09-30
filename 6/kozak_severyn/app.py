#!/usr/bin/python

"""
Team: Severyn Kozak (only)

app, a Python Flask application, populates a template .html
file's empty fields with a randomized selection of words.
Think madlibs.
"""

from flask import Flask, render_template
from random import sample

app = Flask(__name__)

#dictionary of word arrays, by type
wordPool = {'Object' : ['greatsword', 'chalice', 'stacks'], 
			'Verb' 	: ['pilfer', 'hike', 'dungeoneer'], 
			'Place' : ['barrio', 'The Wall', 'Sao Tome'], 
			'Adjective' : ['black', 'svelte', 'gaunt']}

@app.route("/")

#populates template with a shuffled copy of wordPool
def madlib():

	words = {'O': sample(wordPool['Object'], 3),
			'V': sample(wordPool['Verb'], 3),
			'P': sample(wordPool['Place'], 3),
			'A': sample(wordPool['Adjective'], 3)}
	return render_template("template.html", words = words)

if __name__ == "__main__":
	app.run(debug = True)
