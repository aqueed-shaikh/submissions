#!/usr/bin/python

#import sys
import markdown
from flask import Flask
from flask import Markup

app = Flask(__name__)

#if not term:
#    term = raw_input("Look up: ")
@app.route("/")
def home():
    with open("README.md") as docs:
        return Markup(markdown.markdown(docs.read(), smart_emphasis=False))

@app.route("/<term>")
def lookup(term):    
    with open("README.md") as docs:
        content = docs.readlines()
        print "Looking up #%s#"%term
        try:
            index = content.index("#%s#\n"%(term))
        except:
            return "<h1>Term not found.</h1>"
        md = content[index]
        index += 1
        while content[index][0] != "#":
            md += content[index]
            index += 1
        return Markup(markdown.markdown(md))

@app.route("/f/<term>")
@app.route("/funct/<term>")
@app.route("/function/<term>")
def functLookup(term):
    if not "()" in term:
        return lookup(term+"()")
    return lookup(term)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0")
