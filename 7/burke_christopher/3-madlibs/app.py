from flask import Flask
from flask import render_template

import random


app = Flask(__name__)

@app.route("/")
def madlib():
    animal = ('bug','giraffe','dog')
    name = ('Barry','Jon','Arin')
    verb = ('run','explode','dig')
    
    d = {}
    rand = random.randrange(0,len(animal))
    d['ANIMAL'] = animal[rand]

    rand = random.randrange(0,len(name))
    d['NAME'] = name[rand]

    rand = random.randrange(0,len(verb))
    d['VERB'] = verb[rand]
    

    s = "The once was a %(ANIMAL)s named %(NAME)s, who liked to %(VERB)s."

    return render_template("template.html", s=s%(d));

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5005)
