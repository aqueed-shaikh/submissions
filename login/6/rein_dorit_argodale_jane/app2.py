from flask import Flask
from flask import request, render_template, redirect, url_for, session
from flask.ext import shelve
import auth2

app=Flask(__name__)
app.secret_key="key"
app.config['SHELVE_FILENAME'] = 'users.db'
shelve.init_app(app)

@app.route("/")
def homepage():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    if "username" in session:
        return render_template("home.html", session=session)
    else:
	return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        users = shelve.get_shelve()
        if (auth2.usedUsername(username)):
            return render_template("register.html")
        users[username] = password
        session["username"] = username
        return redirect(url_for("home"))

@app.route("/login", methods = ["GET", "POST"]) #placeholder for login page
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        if not auth2.usedUsername(username):
            return 'Invalid username! <a href ="/login"> Please try again.</a>'
        elif auth2.check(username, password) :
            return 'Wrong password! <a href ="/login"> Please try again.</a>'
        session["username"] = username
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop('username')
    return redirect(url_for("login"))


if __name__=="__main__":
    app.debug = True
    app.run()
