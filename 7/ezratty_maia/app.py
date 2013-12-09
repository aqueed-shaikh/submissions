#!/usr/bin/python

from flask import Flask, request, url_for, render_template, session, redirect
from flask.ext import shelve

app = Flask(__name__)
app.config["SHELVE_FILENAME"] = "shelve.db"
app.secret_key = "my secret key"
shelve.init_app(app)


@app.route("/", methods = ["GET", "POST"])
def home():
    if "username" in session:
        return "<h2>You are logged in.</h2>"
    else:
        return redirect("login")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if "username" in session:
        return redirect("home")
    elif request.method == "GET":
        return render_template("register.html", message = "")
    else: 
        userlist = shelve.get_shelve()
        user = request.form["user"]
        pw = request.form["pass"]
        if user in userlist:
            return render_template("register.html", message = "Username already taken.")
        else:
            userlist[user]=pw
            session["username"] = user
            return redirect("home")
        
        

#Make a login page that has a login button and a link to the register page. When you log in, 
#save the username in the session and then redirect to to some other page.
@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
        return redirect("home")
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        userlist = shelve.get_shelve()
        user = request.form["user"].encode("utf8")
        pw = request.form["pass"].encode("utf8")
        if user == "" or pw == "":
            return render_template("login.html", message = "Please try again.")
        elif user not in userlist:
            return render_template("login.html", message = "Username does not exist.")
        elif userlist[user] == pw:
            session["username"] = user
            return redirect("home")
        else:
            return render_template("login.html", message = "User/pass don't match.")

#Make a logout route that pops the username from the session.
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("login")



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=2030)
