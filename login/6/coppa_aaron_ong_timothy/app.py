from flask import Flask
from flask import session,url_for, request, redirect, render_template
import sqlite3,utils

app = Flask(__name__)
app.secret_key="ijasdb012fbrfasdffb0vbevs"

@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html", d=session)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        c = sqlite3.connect("users.db")
        c.execute("create table if not exists users (username TEXT, password TEXT)")
        if (utils.loginauth(username,password)):
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        c = sqlite3.connect("users.db")
        c.execute("create table if not exists users (username TEXT, password TEXT)")
        if (utils.regisauth(username,password)):

        #users = convList([ x for x in (c.execute("SELECT * from users")) ])

        #if users.has_key(username):
         #   return render_template("register.html")
        
        #execstr = 'INSERT INTO users VALUES("' + username + '","' + password + '");'
            #c.execute(execstr)
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return redirect(url_for("register"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

def convList(l):
    d = {}
    for i in l:
        d[i[0]] = i[1]
    return d

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
