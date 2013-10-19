from flask import Flask
from flask import session, url_for, request, redirect, render_template
import sqlite3
import auth

app = Flask(__name__)
app.secret_key="marleyandme"

@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html",username=session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        if (auth.checkuser(username, password)):
            return "Success!"
        else:
            return "Please register!"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        if (not auth.checkuser(username, password)):
            auth.adduser(username, password)
            return "You have created an account"
        else:
            return "User already exists"

@app.route("/reset", methods = ['GET', 'POST'])
def reset():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)
