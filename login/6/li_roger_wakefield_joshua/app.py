# Roger Li and Joshua Wakefield

from flask import Flask
from flask import Flask, session, url_for, request, redirect, render_template
import utils 

app = Flask(__name__)
app.secret_key = "password"

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
	error = utils.login(request.form["username"], request.form["password"]);
    if (error == "notfound"):
        return render_template("login.html", error="usernotfound")
    if (error == "incorrect"):
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
    error = utils.register(request.form["username"], request.form["password"])
    if (error == "exists"):
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
