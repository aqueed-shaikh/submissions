from flask import Flask
from flask import session, url_for, request, redirect, render_template
import sqlite3
import utils

app = Flask(__name__)
app.secret_key="marlyandme"

@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html",username=session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    auth.setup()
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        if (auth.checkuser(username, password)):
            return redirect("/home")
        else:
            return redirect("/home")

@app.route("/register", methods=["GET", "POST"])
def register():
    auth.setup()
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        auth.adduser(username, password)
        users[username] = password
        session['username'] = username
        return redirect("/")

@app.route("/reset", methods = ['GET', 'POST'])
def reset():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)
