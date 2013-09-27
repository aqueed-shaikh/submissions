from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>This is the homepage</h1>"


@app.route("/madlib")
def generate():
  s="""
    One day, %(name)s went to the %(place)s airport. Moments before boarding, %(thing)s 
    fell from his bag. He picked it up and %(verb)s to the gate. %(time)i %(timeunit)s passed 
    and the plane finally lifted off.
    
    """
    
    
