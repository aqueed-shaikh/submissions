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
<p>
Your madlib:
</p>
A long time ago in a galaxy far, far away...
It is a period of civil war. Rebel %(NOUN)s, striking from a hidden base, have won their first %(NOUN)s against the %(ADJECTIVE)s Galactic Empire. During the battle, rebel %(NOUN)s managed to steal %(ADJECTIVE)s plans to the Empire's ultimate weapon, the Death Star, a %(ADJECTIVE)s space station with enough power to %(VERB)s an entire planet. Pursued by the Empire's sinister %(NOUN)s, Princess %(PROPERNOUN)s races home aboard her starship, custodian of the stolen plans that can %(VERB)s her people and restore %(ADJECTIVE)s to the galaxy...

"""
    page = template %(d)
    return page

if __name__ == "__main__":
    app.debug=True
    app.run(host ="0.0.0.0",port = 5000)
