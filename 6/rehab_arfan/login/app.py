from flask import Flask
from flask import request, render_template, redirect, session, url_for
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve'
shelve.init_app(app)
app.secret_key = "my secret key"

@app.route("/")
def index():

@app.route("/home")
def home:
    
@app.route("/login", methods = ['GET', 'POST'])
def login():
    
@app.route("/register", methods = ['GET', 'POST'])
def register():

@app.route("/logout")
def logout:

    
if __name__ = "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)

