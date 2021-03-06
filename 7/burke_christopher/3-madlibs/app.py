from flask import Flask
from flask import render_template

import random

# By Christopher Burke and Nicholas Galasinao

app = Flask(__name__)

@app.route("/madlib1")
def madlib():
    animal = ('bug','giraffe','dog')
    name = ('Barry','Jon','Arin')
    verb = ('run','explode','dig')
    pastverb = ('ate','punched','grabbed')
    adjective = ('red','strange','stupid')
    thing = ('cheeseburger','notebook','keyboard')
    name2 = ('Daniel','Leo','Mark')
    place = ('movie theater','McDonalds','park')
        
    d = {}
    
    rand = random.randrange(0,len(animal))
    d['ANIMAL'] = animal[rand]

    rand = random.randrange(0,len(name))
    d['NAME'] = name[rand]

    rand = random.randrange(0,len(verb))
    d['VERB'] = verb[rand]

    rand = random.randrange(0,len(pastverb))
    d['PASTVERB'] = pastverb[rand]

    rand = random.randrange(0,len(adjective))
    d['ADJECTIVE'] = adjective[rand]

    rand = random.randrange(0,len(thing))
    d['THING'] = thing[rand]
    
    rand = random.randrange(0,len(name2))
    d['NAME2'] = name2[rand]

    rand = random.randrange(0,len(place))
    d['PLACE'] = place[rand]

    s = "There once was a %(ANIMAL)s named %(NAME)s, who liked to %(VERB)s. One day, he %(PASTVERB)s a %(ADJECTIVE)s %(THING)s with his friend %(NAME2)s, but they got bored and went to a %(PLACE)s."
    
    return render_template("template.html", s=s%(d))

@app.route("/madlib2")
def madlibs():
    names = ('Martin','Luis','Paulo', 'Brian', 'Frank')
    place = ('park', 'library', 'Death Star')
    verb2 = ('ran into', 'fought with', 'borrowed money from', 'ate lunch next to')
    thing = ('tree', 'gazebo', 'physics textbook', 'copy of Windows Vista')
    
    a = {}
    
    rand = random.randrange(0,len(names))
    a['NAMES'] = names[rand]

    rand = random.randrange(0,len(place))
    a['PLACE'] = place[rand]
    
    rand = random.randrange(0,len(verb2))
    a['VERB2'] = verb2[rand]

    rand = random.randrange(0,len(thing))
    a['THING'] = thing[rand]

    return render_template("madlibs2.html", a=a)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5005)
