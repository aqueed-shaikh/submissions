#!/usr/bin/python

from random import shuffle
from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    names = ['Suzy','Vivian','Tommy','Brian','Isabella','Judy','Christine']
    places = ['Stuyvesant', 'the park', 'the mall', 'the classroom', 'the mineshaft']
    things = ['carrot', 'bear', 'giraffe', 'refrigerator', 'poker game', 'Tardis']

    shuffle(names)
    shuffle(places)
    shuffle(things)

    s="""
    One day %(name)s was walking in %(place)s.
    %(name)s was very tired when he/she ran into a %(thing)s.
    """

    d = {'name' : names[0],
         'place' : places[0],
         'thing' : things[0]}

    return s%(d)


if __name__ == "__main__":
    app.debug = True
    app.run()
