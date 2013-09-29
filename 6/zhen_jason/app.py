from flask import Flask
from flask import render_template
from random import randrange as rr


app=Flask(__name__)


@app.route("/")
def home():
    return "This is home."

@app.route("/madlib")
def madlib():
    d={
    'pn':['the girl','she','it'],
    'v':['walking','gliding','flying'],
    'pl':['dark alley','basement','subway tracks'],
    'adj':['fat','sweaty','ugly'],
    'noun':['boy','monster','thing']
    }
    return render_template(
        "madlib.html",
        pn  =d['pn']  [rr(0, len(d['pn'])   ) ],
        v   =d['v']   [rr(0, len(d['v'])    ) ],
        pl  =d['pl']  [rr(0, len(d['pl'])   ) ],
        adj =d['adj'] [rr(0, len(d['adj'])  ) ],
        noun=d['noun'][rr(0, len(d['noun']) ) ]
        )

@app.route("/test/")
def test():
    return render_template("test.html",name="Jason")

if __name__=="__main__":
    app.run(host= "0.0.0.0", port=4646)
