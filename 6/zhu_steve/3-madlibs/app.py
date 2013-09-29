# TEAM MEMBERS: JASPER LU & STEVE ZHU

import random
import re

from word import Word

from flask import Flask
from flask import render_template


app = Flask(__name__)

WORDS = {
    'name': ('Steve', 'Jasper', 'Roger', 'Ben', 'Jing', 'Jason', 'Marlena', 'Jane', 'Pascu'),
    'noun': ('laptop', 'clock', 'chair', 'gun', 'clock', 'toilet'),
    'verb': ('run', 'shoot', 'kill', 'steal', 'save', 'nap'),
    'adjective': ('fabulous', 'harmonious', 'wordy', 'slow', 'fast', 'dumb'),
    'place': ('McDonalds', 'Sydney', 'Burger King', 'the Sahara', 'Google Headquarters')
}
COUNTS = {
    'name': 2,
    'noun': 1,
    'verb': 1,
    'adjective': 1,
    'place': 1
}

@app.route("/")
def madlibs():
    WORDS = {key: [Word(w) for w in WORDS[key]] for key in WORDS}
    print words
    return render_template('madlibs.html', w = WORDS)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5005)
