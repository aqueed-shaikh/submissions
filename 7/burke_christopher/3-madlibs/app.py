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
    rand = random.randrange(0,3)
    d['ANIMAL'] = animal[rand]
    

    s = "The once was a %(ANIMAL)s named %(NAME)s, who liked to %(VERB)s."

    return render_template("template.html", s=s);
