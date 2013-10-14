# Roger Li and Joshua Wakefield

from flask import Flask
from flask import Flask, session, url_for, request, redirect, render_template
from flask.ext import shelve
import sqlite3, utils 

app = Flask(__name__)
app.config["SHELVE_FILENAME"] = "login.db"
app.secret_key = "password"
shelve.init_app(app)

@app.route("/")
def index():
    if ("username" in session):
        return render_template("index.html", username=session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")
    username, password = (request.form["username"].encode("utf8"), request.form["password"].encode("utf8"))
    if (!username || !password):
        return render_template("login.html", error="empty")
	SQL_Users = sqlite3.connect('SQL_Users')
    if (!utils.userNameExist(SQL_Users,username)):
        return render_template("login.html", error="usernotfound")
    if (!utils.authenticate(SQL_Users,username,password)):
        return render_template("login.html", error="incorrect")
    session["username"] = username
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if (request.method == "GET"):
        return render_template("register.html")
    username, password = (request.form["username"].encode("utf8"), request.form["password"].encode("utf8"))
    if (!username or !password):
        return render_template("register.html", error="empty")
    SQL_Users = sqlite3.connect('SQL_Users')
    if (utils.userNameExist(SQL_Users,username)):
        return render_template("register.html", error="taken")
    db[username.lower()] = password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
