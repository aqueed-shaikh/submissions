from flask import Flask
from flask import render_template

import random

madlibs = Flask(__name__)

d={'people':['Bob','Jane'],
   'verbs':['jump','walk'],
   'things':['bat','sandwich','money'],
   'adverbs':['quickly','sexily','arduously'],
   'places':['park','store','gym']
   }

@madlibs.route("/")
def site():
    return render_template("madlibs.html",d=d)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
