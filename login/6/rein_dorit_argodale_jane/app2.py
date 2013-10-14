from flask import Flask
from flask import request, render_template, redirect, url_for, session
from flask.ext import shelve
import sqlite3
import auth


app=Flask(__name__)
app.secret_key="key"
app.config['SHELVE_FILENAME'] = 'users.db'
shelve.init_app(app)

@app.route("/home")
def home():
    if "username" in session:
        return "<h1>Hello!</h1>"
    else:
	return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    New_users = sqlite3.connect('SQL_users')    
    New_users.execute('''
    CREATE TABLE if not exists auth (username TEXT, password TEXT)
    ''')
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
       if New_users.usedUSername(New_users, username) == 1:
            return render_template("register.html")
        else:
            New_users.add(New_users, username, password)
            return redirect(url_for("home"))

@app.route("/login", methods = ["GET", "POST"]) 
def login():
    New_users = sqlite3.connect('SQL_users')    
    users_SQL = New_users.cursor()
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        if auth.authenticate(New_users, username, password) == 1:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for("login"))

if __name__=="__main__":
    app.debug = True
    app.run()
