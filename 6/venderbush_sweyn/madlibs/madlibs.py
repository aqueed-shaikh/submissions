from flask import Flask
from flask import render_template
import shelve
from random import choice
app = Flask(__name__)

words={}
nouns=["ninja", "chair", "pancake", "statue", "unicorn", "rainbow", "laser beam", "senor", "bunny", "captain", "nibblet", "cupcake", "carrot", "gnome", "glitter", "potato", "salad", "toejam", "curtain"]
adjectives=["shining", "crispy", "soaring", "endless", "sparkling", "fluttering", "spiky", "scrumptious", "eternal", "slimy", "slick", "gilded", "ancient", "smelly", "glowing", "rotten", "decrepit", "lousy", "grimy", "rusty", "sloppy", "muffled", "foul", "rancid", "fetid"]
names = ["Jim", "Felix", "Rochanelle", "Liquanaishanda", "Sweynaynagram", "Sean Toodle" ]
verbs = ["paint", "dance", "swim", "twerk"]
places = ["Tihuana", "Aruba", "Jupiter", "South Australia" ]
words['verb'] = verbs
words['noun'] = nouns
words['adjective'] = adjectives
words['name'] = names
words['place'] = places

def initDict():
	genesis = shelve.open("values/genesis")
	genesis['noun'] = 3
	genesis['name'] = 1
	genesis['adjective'] = 2
	genesis['verb'] = 3
	genesis['place'] = 1
	genesis.close()
	exodus = shelve.open("values/exodus")
	exodus['noun'] = 0
	exodus['name'] = 2
	exodus['adjective'] = 2
	exodus['verb'] = 2
	exodus['place'] = 1
	exodus.close()

def createDict(d):
    passDict = {}
    for key in d:
	for i in range(d[key]):
		passDict[key+str(i)] = choice(words[key])
    return passDict

@app.route("/")
@app.route("/<name>")
def root(name="genesis"):
    values = shelve.open("values/" + name)
    d=createDict(values)
    return render_template(name + ".html", d=d)

@app.route('/favicon.ico')
def favicon():
    pass

if __name__ == "__main__":
    initDict()
    app.run()

