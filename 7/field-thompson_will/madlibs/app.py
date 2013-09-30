from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

templates = ['test.html'] #add file names of html templates from which to pick
nouns = ['block', 'guitar', "Mr. Zamansky's beard", "Mr. Brown's hair", "golf club", "golf ball"]
tverbs = ['ran', 'walked', 'swam', 'floated', 'flew', 'escaped', 'hopped', 'skipped'] #verbs to do with moving
names = ['Mr. Zamansky', 'Mr. Brown', 'Mr. Brooks', 'Mr. DW', 'Mr. K', 'Mr. Platek', 'Thluffy']
places = ['Stuyvesant High School', 'TriBeCa', 'chez Hunter', 'the International Space Station', 'Atlantis']
adjectives = ['happy', 'sad', 'angry', 'confused', 'blue', 'chartreuse', 'perplexed', 'holy']


       
def noun():
	return random.choice(nouns);
def verb():
	return random.choice(tverbs);
def place():
	return random.choice(places);
def adjective():
	return random.choice(adjectives);
def name():
	return random.choice(names);
@app.route("/")
def home():
    return render_template(random.choice(templates), noun=noun,verb=verb,name=name,place=place,adjective=adjective)

if (__name__ == "__main__"):
    app.debug = True
    app.run("0.0.0.0")


