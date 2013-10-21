#!/usr/bin/python

#Judy Mai & Maia Ezratty 

from flask import Flask, request, url_for, render_template, session, redirect
from auth import adduser, authenticate, changepw 

app = Flask(__name__)
app.secret_key = "my secret key"


@app.route("/", methods = ["GET", "POST"])
def home():
    if "username" in session:
        return "<h2>You are logged in.</h2>"
    else:
        return redirect(url_for("login"))


@app.route("/register", methods = ["GET", "POST"])
def register():
    if "username" in session:
        return redirect("home")
    elif request.method == "GET":
        return render_template("register.html", message = "")
    else: 
        user = request.form["user"].encode("utf8")
        pw = request.form["pass"].encode("utf8")
        if adduser(user, pw):
            return redirect("login")
        else:
	    return render_template("register.html", message = "Username already taken.")
            
        
        
#Make a login page that has a login button and a link to the register page. When you log in, 
#save the username in the session and then redirect to to some other page.
@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
        return redirect("home")
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        user = request.form["user"].encode("utf8")
        pw = request.form["pass"].encode("utf8")
        if user == "" or pw == "":
            return render_template("login.html", message = "Please try again.")
        elif authenticate(user, pw):
            session["username"] = user
            return redirect("home")
        else:
            return render_template("login.html", message = "User/pass don't match.")


@app.route("/changepw")
def changepw():
	if "username" in session:
            if request.method == "GET":
                return render_template("changepw.html", message = "")
            else:
                oldpw = request.form["oldpw"].encode("utf8")
                newpw = request.form["newpw"].encode("utf8")
                if changepw(session["username"], oldpw, newpw):
                    return redirect("login")
                else:
                    return redirect("changepw.html", message = "Please try again.")	
	else:
            return redirect("login")		


#Make a logout route that pops the username from the session.
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("login")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5004)
