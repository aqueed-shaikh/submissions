from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

blanks = {
    'NAMES': ['Elmo','Pikachu','Sheldon','Batman','Mr. Z'],
	'PRONOUNS': ['he','she','they','me','you','we'],
    'NOUNS': ['potatoes','lollipops','tornadoes','peanut butter','bacon','dollars'],
    'ADJS': ['crazy','big','stinky','lonely','boring'],
    'VERBS': ['sing','PMS', 'sleep'],
    'ADVS': ['lovingly','happily','crazily','angrily']
}

@app.route("/")
def home():
    return "<h1>This is the home page</h1>"

@app.route("/madlibs")
def madlibs():
    return render_template("madlibs.html",
		name1 = blanks['NAMES'][random.randrange(0,len(blanks['NAMES']))],
		name2 = blanks['NAMES'][random.randrange(0,len(blanks['NAMES']))],
		name3 = blanks['NAMES'][random.randrange(0,len(blanks['NAMES']))],
		pro1 = blanks['PRONOUNS'][random.randrange(0,len(blanks['PRONOUNS']))],
		pro2 = blanks['PRONOUNS'][random.randrange(0,len(blanks['PRONOUNS']))],
		noun1 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		noun2 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		noun3 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		noun4 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		noun5 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		noun6 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		noun7 = blanks['NOUNS'][random.randrange(0,len(blanks['NOUNS']))],
		adj1 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		adj2 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		adj3 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		adj4 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		adj5 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		adj6 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		adj7 = blanks['ADJS'][random.randrange(0,len(blanks['ADJS']))],
		verb1 = blanks['VERBS'][random.randrange(0,len(blanks['VERBS']))],
		verb2 = blanks['VERBS'][random.randrange(0,len(blanks['VERBS']))],
		verb3 = blanks['VERBS'][random.randrange(0,len(blanks['VERBS']))],
		adverb1 = blanks['ADVS'][random.randrange(0,len(blanks['ADVS']))],
		adverb2 = blanks['ADVS'][random.randrange(0,len(blanks['ADVS']))],
		adverb3 = blanks['ADVS'][random.randrange(0,len(blanks['ADVS']))],
	)

if __name__ == "__main__":
    app.debug=True
    app.run()
