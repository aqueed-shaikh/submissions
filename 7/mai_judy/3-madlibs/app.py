#!/usr/bin/python

#Judy Mai & Isabella Siu

from random import shuffle
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test():
    names = ['Suzy','Vivian','Tommy','Brian','Isabella','Judy','Christine']
    places = ['Stuyvesant', 'the park', 'the mall', 'the classroom', 'the mineshaft']
    things = ['carrot', 'bear', 'giraffe', 'refrigerator', 'poker game', 'Tardis']

    shuffle(names)
    shuffle(places)
    shuffle(things)


    d = {'name' : names[0],
         'place' : places[0],
         'thing' : things[0]}

    return render_template('madlibs.html', d=d)


if __name__ == "__main__":
    app.debug = True
    app.run()
