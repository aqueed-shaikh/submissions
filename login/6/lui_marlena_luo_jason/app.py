from flask import Flask
from flask import session, url_for, request, redirect, render_template
#import sqlite3
#import auth
import utils

app = Flask(__name__)
app.secret_key="marleyandme"

@app.route("/", methods=["GET", "POST"])
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
        if (utils.checkuser(username, password)) == 0:
            session["username"] = username
            return redirect("/success")
        if (utils.checkuser(username, password)) == 1:
            print "username does not exist. please register."
            return redirect("/register")
        if (utils.checkuser(username, password)) == 2:
            print "password does not match username. please try again."
            return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        button = request.form["button"]
        if button == "register":
            username = request.form["username"].encode("ascii", "ignore")
            password = request.form["password"].encode("ascii", "ignore")
            if not utils.adduser(username, password):
                print "this username already exists. please pick another."
                return redirect("/register")
            session["username"] = username
            return redirect("/success")
                    
        #if (not auth.checkuser(username, password)):
         #   auth.adduser(username, password)
          #  return "You have created an account"
       # else:
        #    return "User already exists"


@app.route("/reset", methods = ['GET', 'POST'])
def reset():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/success")
def success():
    return "<h1> you have logged in successfully. congratz. </h1>"

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)

