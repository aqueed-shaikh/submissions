from flask import Flask
from flask import request
from flask import url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is the Home Page</h1>"

@app.route("/register", methods=["POST","GET"])
def register():
    
