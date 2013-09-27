from flask import Flask
from flask import render_template
from random import random

app = Flask(__name__)

@app.route("/madlibs")
def madlibs():
    d = {'name': 'Josh',
         'verb1': 'walking',
         'place': 'park',
         'verb2': 'run over',
         'thing': 'snake'}
    return render_template("madlibs1.html", d=d);
