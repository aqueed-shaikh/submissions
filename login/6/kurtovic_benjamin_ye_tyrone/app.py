# Benjamin Kurtovic and Tyrone Ye

from flask import Flask
from flask import Flask, session, url_for, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config["SHELVE_FILENAME"] = "login.db"
shelve.init_app(app)
app.secret_key = "nLOGN"

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html")
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form["username"].lower().encode("utf8")
    password = request.form["password"].encode("utf8")
    if not username or not password:
        return render_template("login.html", error="Missing a username or password.")
    db = shelve.get_shelve()
    if username not in db:
        return render_template("login.html", error="Username does not exist.")
    if db[username] != password:
        return render_template("login.html", error="Incorrect password.")
    session["username"] = username
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    username = request.form["username"].lower().encode("utf8")
    password = request.form["password"].encode("utf8")
    if not username or not password:
        return render_template("register.html", error="Missing a username or password.")
    db = shelve.get_shelve()
    if username in db:
        return render_template("register.html", error="Username already exists.")
    db[username] = password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username", None)
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
