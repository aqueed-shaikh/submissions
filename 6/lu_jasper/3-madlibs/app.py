# TEAM MEMBERS: JASPER LU & STEVE ZHU

import random
import re

from word import Word

from flask import Flask
from flask import render_template

def shuffle(list):
    random.shuffle(list)
    return list

app = Flask(__name__)

WORDS = {
    'name': ('Steve', 'Jasper', 'Roger', 'Ben', 'Jing', 'Jason', 'Marlena', 'Jane', 'Pascu'),
    'noun': ('laptop', 'clock', 'chair', 'gun', 'clock', 'toilet'),
    'verb': ('run', 'shoot', 'kill', 'steal', 'save', 'nap'),
    'adjective': ('fabulous', 'harmonious', 'wordy', 'slow', 'fast', 'dumb'),
    'place': ('McDonalds', 'Sydney', 'Burger King', 'the Sahara', 'Google Headquarters')
}

@app.route("/")
def madlibs():
    w = {key: shuffle([Word(w) for w in WORDS[key]]) for key in WORDS}
    return render_template('madlibs.html', w = w)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)