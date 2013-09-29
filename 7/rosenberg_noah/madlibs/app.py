#!/usr/bin/python

from flask import Flask
from random import randrange

NOUNS[] = {'apple', 'bus', 'candle','dolphin','elephant','flask','guillotine',
           'harp','isthmus', 'jackass', 'king','lemon','mensch','nudist',
           'orifice','penguin','quark','raccoon','schlemiel','transvestite',
           'undergarment','vanity','wingman','xenophobe','yurt','zebra'}

VERBS[] = {'ate', 'baked', 'caressed','dared','earned','fought','generated',
           'hurt','irked'}

ADJECTIVES[] = {'artsy','ballistic','crazy','drunk','energetic','fallacious',
                'greedy','hellish','irritating','Jewish','kind','long',
                'mighty','near-perfect','open','pensive','quirky','rapid',
                'shining'}

PROPER_NOUNS[] = {'Aaron','Bob','Chris','David','Fabian','Harry','Ingrid',
                  'Jason','Liz','Martha','Noah','Quentin','Sarah'}

ADVERBS[] = {'briskly','creatively','dashingly','earnestly','freely'}

#returns random word from wordlist
def randWord(x[]): 
    rand = randrange(len(x))
    return x[rand]

app = Flask(__name__)

@app.route("/")
def madlibs():
    return template.html

