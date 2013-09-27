from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>This is the homepage</h1>"

@app.route("/madlib")
def madlib():
  
