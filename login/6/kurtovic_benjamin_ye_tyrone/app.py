# Benjamin Kurtovic and Tyrone Ye

from flask import Flask
from flask import Flask, session, request, redirect, render_template

import utils

app = Flask(__name__)
app.secret_key = "Ben_Tyrone_L0G!N"

def fail(template, error):
    return render_template(template + ".html", error=error)

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    error = utils.login(request.form["username"], request.form["password"])
    if not error:
        session["username"] = request.form["username"]
        return redirect("/")
    else:
        return fail("login", error)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    error = utils.register(request.form["username"], request.form["password"])
    if not error:
        session["username"] = request.form["username"]
        return redirect("/")
    else:
        return fail("register", error)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
