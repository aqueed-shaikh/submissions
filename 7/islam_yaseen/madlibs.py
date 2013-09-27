from flask import Flask
from flask import render_template

import random

madlibs = Flask(__name__)

template="""
<h1>Well here you go</h1>

<p>%(name1)s decided to %(adverb1)s %(verb1)s to the %(place1)s.</p>
"""

verb_list=['jump','walk','slide']
name_list=['Bob','Jane']
thing_list=['bat','sandwich','money']
adverb_list=['quickly','arduously','sexily']
place_list=['park','store','gym']




@madlibs.route("/")
def site():
    d={'name1':name_list[(random.random()*len(name_list))],
       'verb1':verb_list[(random.random()*len(verb_list))],
       'thing1':thing_list[(random.random()*len(thing_list))],
       'adverb1':adverb_list[(random.random()*len(adverb_list))],
       'place1':place_list[(random.random()*len(place_list))]]
    }
    return template%(d

if __name__=="__main__":
    madlibs.debug=True
    madlibs.run(host="0.0.0.0",port=5005)
