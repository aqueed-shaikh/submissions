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
    if "username" in session:
        return redirect("/")
    elif request.method == "GET":
        return render_template("login.html");
    else:
        usrname = request.form["username"]
        pw = request.form["password"]
        shelve[usrname] = pw

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username", None)
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
