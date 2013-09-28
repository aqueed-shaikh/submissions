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
    fell from his bag. He picked it up and %(verb)s to the gate. %(num)i %(timeunit)s passed 
    and the plane finally lifted off. When the %(adj)% flight attendant approached him asking if he
    wanted something to drink, he reponded with, "I would like %(drink)s please." The attendant filled
    up the cup with %(drink)s instead and was about to hand it over, but spilled it all over. At that very 
    moment, the %(adj)s flight captain fell asleep, and so did the co-pilot, so the plane went out of control.
    %(num)i %(timeunit)s later, the plane crashed onto an uncharted island. There were %(time)i casualties. 
    At that time, %(num)i supposedly extinct creatures surrounded them and ate them all. And then there were none.
    p.s. There are two references in here! 
    """
    
    
