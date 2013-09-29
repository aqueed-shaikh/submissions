#!/usr/bin/python
from flask import Flask
import random

app = Flask(__name__)
@app.route("/madlibs")


def madlibs():
    i = random.randint(1,10)

    
    pr =["Lilo", "Stitch", "Nemo", "Elmo", "Shrek", "Spongebob", "Bill", "Plankton", "Sandy", "Squishy"]
    vb = ["galloping", "paddling", "discouraging", "spinning", "running", "stabbing", "tickling", "shrieking", "folding", "eating"]
    pl = ["BMCC", "sushi buffet", "Duane Read", "roof", "cupboard under the stairs", "room 305", "Narnia", "pokeball", "cow", "helicopter", "Starbucks", "Chipotle", "12 Grimmauld Place", "my apartment"]
    ad = [ "ugly", "really ugly", "sparkling", "querulous", "facetious", "fulminating" , "phlegmatic", "laconic", "tortuous", "pussilanimous"]
    ns = [ "trashcan" , "building", "phone", "cactus", "sun", "folder", "car", "shirt", "fruits", "hair", "lychee"]
    
    d = { 'PROPERNOUN' : random.choice(pr),
          'VERB' : random.choice(vb),
          'PLACE' : random.choice(pl),
          'ADJECTIVE' : random.choice(ad),
          'NOUN' : random.choice(ns)
          }

    template = """
<h1> Madlibs! </h1>
Project by: Jason Luo, Marlena Lui

<h2>Your madlib:</h2>
"One day %(PROPERNOUN)s was %(VERB)s through the %(PLACE)s. There he found a(n) %(ADJECTIVE)s %(NOUN)s."

"""
    page = template %(d)
    return page

if __name__ == "__main__":
    app.debug=True
    app.run(host ="0.0.0.0",port = 5000)
