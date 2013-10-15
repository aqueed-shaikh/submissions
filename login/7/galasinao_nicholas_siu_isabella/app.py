#!/usr/bin/python

from flask import Flask, session, request, url_for, render_template, redirect
import auth
import sqlite3

app = Flask(__name__)
app.secret_key="magic"

@app.route("/")
def home():
    if "username" in session:
        return "<h1>This is the Home Page</h1>"
    else:
        return redirect("/login")

@app.route("/register", methods=["POST","GET"])
def register():
    database = sqlite3.connect('names.db')
    database.execute('''
    CREATE TABLE if not exists user(username text, password text)
''')
    if request.method=="GET":
        return render_template("register.html")
    else:
        username=request.form["username"].encode("ascii","ignore")
        password=request.form["password"].encode("ascii","ignore")
        if request.form["button"]=="Submit":
            if auth.exists(username):
                return render_template("register.html")
            else:
                auth.adduser(username,password)
                return render_template("success.html",username=username)
        else:
            return render_template("register.html")
            
@app.route("/login", methods=["POST","GET"])
def login():
    database = sqlite3.connect('names.db')
    if request.method=="GET":
        return render_template("login.html")
    else:
        username=request.form["username"].encode("ascii","ignore")
        password=request.form["password"].encode("ascii","ignore")
        if auth.authenticate(username,password):
            session["username"]=username
            return redirect("/")
        else:
            return redirect("/login")
            
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
