#!/usr/bin/python

from flask import Flask, session, request, url_for, render_template, redirect
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME']= 'users.db'
app.secret_key="magic"
shelve.init_app(app)

@app.route("/")
def home():
    if "username" in session:
        return "<h1>This is the Home Page</h1>"
    else:
        return redirect("/login")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        users=shelve.get_shelve()
        username=request.form["username"].encode("ascii", "ignore")
        password=request.form["password"].encode("ascii", "ignore")
        if request.form["button"]=="Submit":
            users[username]=password
            return render_template("success.html",username=username)
        else:
            return render_template("register.html")
            
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        users=shelve.get_shelve()
        username=request.form["username"].encode("ascii", "ignore")
        password=request.form["password"].encode("ascii", "ignore")
        if username in users:
            if password==users[username]:
                session["username"]=username
                return redirect("/")
            else:
                return redirect("/login")
        else:
            return redirect("/register")

#<<<<<<< HEAD
@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/login")

@app.route("/secret")
def secret():
    if "username" in session:
        return "<h1>A wild Secret appeared!</h1>"
    else:
        return redirect("/login")

#>>>>>>> 5762cfd68f458a814eb675ba67b2a2e421eb5552

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=7777)
