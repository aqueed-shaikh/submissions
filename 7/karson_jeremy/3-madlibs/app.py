#!/usr/local/bin/python

#team members: Benjamin Attal and Jeremy Karson

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

mlibs = {
    'stories': {},
    'inputs': {}
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

@app.route("/")
def index():
  return render_template('index.html', files=mlibs['stories'])

@app.route("/input/")
@app.route("/input/<name>")
def madlib(name='story1'):
  return render_template('lib.html', words=mlibs['inputs'][name], file=name)


@app.route("/results/")
@app.route("/results/<name>", methods=['GET', 'POST'])
def results(name='story1'):
  if request.method == 'POST':
    return mlibs['stories'][name] % request.form
  else:
    return redirect(url_for('madlib') + name)

if __name__ == '__main__':
  app.run(debug=True)
