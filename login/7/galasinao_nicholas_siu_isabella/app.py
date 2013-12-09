#!/usr/bin/python

from flask import Flask, session, request, url_for, render_template, redirect
import auth
import pymongo

app = Flask(__name__)
app.secret_key="magic"
client = pymongo.MongoClient()

@app.route("/")
def home():
    if "username" in session:
        return "<h1>This is the Home Page</h1>"
    else:
        return redirect("/login")

@app.route("/register", methods=["POST","GET"])
def register():
    database = client.userdb
    collection = database.usercol
    if request.method=="GET":
        return render_template("register.html")
    else:
        username=request.form["username"].encode("ascii","ignore")
        password=request.form["password"].encode("ascii","ignore")
        if request.form["button"]=="Submit":
            if auth.exists(username):
                return render_template("success.html",username=username)
            else:
                auth.adduser(username,password)
                return render_template("login.html")
        else:
            return render_template("register.html")
            
@app.route("/login", methods=["POST","GET"])
def login():
    database = client.userdb
    collection = database.usercol
    if request.method=="GET":
        return render_template("login.html")
    else:
        username=request.form["username"].encode("ascii","ignore")
        password=request.form["password"].encode("ascii","ignore")
        if auth.exists(username):
            if auth.authenticate(username,password):
                session["username"]=username
                return redirect("/")
            else:
                return redirect("/login")
        else:
            return redirect("/register")
            
#<<<<<<< HEAD
@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
    return redirect("/login")

@app.route("/change")
def change():
    database = client.userdb
    collection = database.usercol
    if request.method=="GET":
        return render_template("change.html")
    else:
        username=request.form["username"].encode("ascii","ignore")
        oldPw=request.form["old password"].encode("ascii","ignore")
        newPw=request.form["new password"].encode("ascii","ignore")
        if auth.exists(username):
            if auth.authenticate(username,password):
                auth.changePw(username, oldPw, newPw)
                return redirect("/")
            else:
                return redirect("/login")
        else:
            return redirect("/register")

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
