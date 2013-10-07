from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
from flask.ext import shelve
import login
app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html")
@app.route("/login")
def login():
    return render_template ("login.html")
@app.route("/register")
def register():
    return render_template ("register.html")





if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6969)
