from flask import Flask
from flask import render_template
import shelve
from random import choice
app = Flask(__name__)

words={}
nouns=["ninja", "chair", "pancake", "statue", "unicorn", "rainbows", "laser beams", "senor", "bunny", "captain", "nibblets", "cupcake", "carrot", "gnome", "glitter", "potato", "salad", "toejam", "curtain"]
adjectives=["shining", "crispy", "soaring", "endless", "sparkling", "fluttering", "spiky", "scrumptious", "eternal", "slimy", "slick", "gilded", "ancient", "smelly", "glowing", "rotten", "decrepit", "lousy", "grimy", "rusty", "sloppy", "muffled", "foul", "rancid", "fetid"]
names = ["jim", "felix", "rochanelle", "liquanaishanda", "sweynaynagram", "sean toodle" ]
verbs = ["paint", "dance", "swim", "twerk"]
places = ["Tihuana", "Aruba", "Jupiter", "South Austrailia" ]
words['verb'] = verbs
words['noun'] = nouns
words['adjective'] = adjectives
words['name'] = names
words['place'] = places
def initDict():
	Genesis = shelve.open("values/genesis")
	Genesis['noun'] = 3
	Genesis['name'] = 1
	Genesis['adjective'] = 2
	Genesis['verb'] = 3
	Genesis['place'] = 1
	Genesis.close()
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
    print(d)
    return render_template(name + ".html", d=d)

@app.route('/favicon.ico')
def favicon():
    pass

if __name__ == "__main__":
    app.run()

