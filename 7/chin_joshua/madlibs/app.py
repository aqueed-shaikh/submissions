#! /usr.bin/env python
#Joshua Chin

from flask import Flask, render_template
import madlib

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('madlibs.html', story = madlib.main())
