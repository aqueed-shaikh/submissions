from flask import Flask
from flask import render_template

import random

madlibs = Flask(__name__)

template="""
<h1>Well here you go</h1>

<p>%(people)s decided to %(verbs)s to the %(places)s.</p>
"""

d={'people':'Bob'#,'Jane'],
   'verbs':'jump'#,'walk'],
   'things':'bat'#,'sandwich','money'],
   'adverbs':'quickly'#,'sexily','arduously'],
   'places':'park'#,'store','gym']
   }

@madlibs.route("/")
def site():
    return template(d)

if __name__=="__main__":
    madlibs.debug=True
    madlibs.run(host="0.0.0.0",port=5005)
