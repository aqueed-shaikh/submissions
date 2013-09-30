#!/usr/local/bin/python
"""

from Benjamin Attal and Jeremy Karson
pd 7

"""

from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

mlibs = {
    'stories': {},
    'inputs': {},
}

pos = {
    'NOUN': ['dog', 'cat', 'clock', 'day', 'sun', 'moon', 'poop', 'fart', 'cow', 'cow pie', 'fruit fly', 'octopus', 'king crab'],
    'VERB': ['fart', 'smell', 'lick', 'kick', 'stun', 'punch', 'grab', 'eat', 'roll over', 'scratch', 'fight'],
    'PLACE': ['market', 'six flags', 'greece', 'venezuela', 'mt. st. helens', 'volcano', 'general store', 'fight club'],
    'PROFESSION': ['trumpeteer', 'horse', 'horse rider', 'dog walker', 'cat trainer', 'cattle rancher', 'insurance salesesman'],
    'PLURAL_NOUN': ['clocks'],
    'ADJECTIVE': ['smelly', 'brown', 'neon purple', 'cushy', 'comfortable', 'chair-like', 'hairy'],
    'PRONOUN': ['he', 'she', 'it', 'tuna']
}

for root, dir, files in os.walk("mlibs"):
  for f in files:
    story = ''.join(open(os.path.join(root, f)).readlines())
    list = []
    for item in story.split('%('):
      if item.find(')s') == -1:
        continue
      list.append(item[:item.find(')s')])
    mlibs['stories'][f[:f.find('.mlib')]] = story
    mlibs['inputs'][f[:f.find('.mlib')]] = list

def readable(s):
  return no_digits(s.replace('_', ' ').lower())

def no_digits(s):
  return ''.join(c for c in s if not c.isdigit())

@app.route("/")
def index():
  return render_template('index.html', files=mlibs['stories'])

@app.route("/input/")
@app.route("/input/<name>")
def madlib(name='story1'):
  words = {}
  for i in mlibs['inputs'][name]:
    words[i] = readable(i)
  return render_template('lib.html', words=words, file=name)

@app.route("/results/")
@app.route("/results/<name>", methods=['GET', 'POST'])
def results(name='story1'):
  if request.method == 'POST':
    return mlibs['stories'][name] % request.form
  else:
    return redirect(url_for('madlib') + name)

@app.route("/random/")
@app.route("/random/<name>")
def randomlib(name='story1'):
  words = {}
  for i in mlibs['inputs'][name]:
    words[i] = random.choice(pos[no_digits(i)])
  return mlibs['stories'][name] % words

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
