#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import url_for,render_template,redirect
import db

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h3> THIS IS THE HOME PAGE! THIS LINKS WILL TAKE YOU WHERE YOU NEED TO GO! </h3>
<br>
<a href="/signup"> Sign Up! </a>
<br>
<a href="/login"> Login </a>
"""

@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        d={'uname':request.form['uname'],'pword':request.form['pword']}
        if request.form['button']=="Submit":
            db.add(d['uname'],d['pword'])
            return redirect(url_for('login'))
        else:
            return render_template("signup.html")


@app.route("/<username>")
def user(username):
    return render_template("user.html", username = username)

@app.route("/login", methods=["POST","GET"])
def login():

    if request.method=="GET":
        return render_template("login.html", message = "")

    d={'uname':request.form['uname'],'pword':request.form['pword']}
    if request.form['button']=="Submit":

        if db.login(d['uname'],d['pword']):
            return redirect(url_for('user', username = d['uname']))

        return render_template("login.html", message = "error, invalid username-password combination")

    return render_template("login.html", message = "")



if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=5000)
