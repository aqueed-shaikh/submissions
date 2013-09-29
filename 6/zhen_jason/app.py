from flask import Flask
from flask import render_template
from random import randint as ri


app=Flask(__name__)


@app.route("/")
def home():
    return "This is home."

@app.route("/madlib")
def madlib():
    d={
    'pn':['The girl','she','it'],
    'v':['walking','gliding','flying'],
    'pl':['dark alley','basement','subway tracks'],
    'adj':['fat','sweaty','ugly'],
    'noun':['boy','monster','thing']
    }
    return render_template(
        "madlib.html",
        pn=d['pn'][ri(0,2)],
        v=d['v'][ri(0,2)],
        pl=d['pl'][ri(0,2)],
        adj=d['adj'][ri(0,2)],
        noun=d['noun'][ri(0,2)]
        )

@app.route("/test/")
def test():
    return render_template("test.html",name="Jason")

if __name__=="__main__":
    app.run(debug=True)
