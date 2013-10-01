from flask import Flask
from flask import render_template
import random

madlibs = Flask(__name__)

template="""
<h1>Madlibs</h1>

<p>%(name1)s was %(adverb1)s %(verb1)s down the %(place1)s with %(name2)s. However, they saw a %(adj1)s %(thing1)s.</p>
"""


@madlibs.route("/")
def site():
    verb_list=['walking','speeding','biking','teleporting','skateboarding','rollerblading','rowing']
    name_list=['Bob','Jane','Donald','Mr Z','Superman']
    thing_list=['bird','goat','cookie','Pokemon','jewel','lamp','fan']
    adverb_list=['hastily','slowly','quietly']
    place_list=['street','beach','sidewalk','park','alleyway','battlefield','classroom']
    adj_list=['yellow','green','gold','flying','smelly']
    
    
    d={'name1':name_list.pop(int(random.random()*len(name_list))),
       'verb1':verb_list.pop(int(random.random()*len(verb_list))),
       'thing1':thing_list.pop(int(random.random()*len(thing_list))),
       'adverb1':adverb_list.pop(int(random.random()*len(adverb_list))),
       'place1':place_list.pop(int(random.random()*len(place_list))),
       'name2':name_list.pop(int(random.random()*len(name_list))),
       'adj1':adj_list.pop(int(random.random()*len(adj_list)))
    }
    return template%(d)

if __name__=="__main__":
    madlibs.debug=True
    madlibs.run(host="0.0.0.0",port=5001)
