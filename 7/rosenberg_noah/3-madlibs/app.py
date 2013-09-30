#!/usr/bin/python
#group members: Noah Rosenberg & Shaan Sheikh

from flask import Flask, render_template
from random import randrange

NOUNS = ['apple', 'bus', 'candle','dolphin','elephant','flask','guillotine',
           'harp','isthmus', 'jackass', 'king','lemon','mensch','nudist',
           'orifice','penguin','quark','raccoon','schlemiel','transvestite',
           'undergarment','vanity','wingman','xenophobe','yurt','zebra']

VERBS = ['ate', 'baked', 'caressed','dared','earned','fought','generated',
           'hurt','irked']

ADJECTIVES = ['artsy','ballistic','crazy','drunk','energetic','fallacious',
                'greedy','hellish','irritating','Jewish','kind','long',
                'mighty','near-perfect','open','pensive','quirky','rapid',
                'shining']

PROPER_NOUNS = ['Aaron','Bob','Chris','David','Fabian','Harry','Ingrid',
                  'Jason','Liz','Martha','Noah','Quentin','Sarah']

ADVERBS = ['briskly','creatively','dashingly','earnestly','freely']

#returns random word from wordlist
def randWord(x): 
    rand = randrange(len(x))
    return x[rand]

app = Flask(__name__)



@app.route("/")
def madlibs():
    proper_noun1 = randWord(PROPER_NOUNS)
    noun1 = randWord(NOUNS)
    adj1 = randWord(ADJECTIVES)
    return render_template('madlibs.html', proper_noun1 = proper_noun1,
                           noun1 = noun1, adj1 = adj1)


app.run(debug = True,host = "0.0.0.0",port = 5621)
