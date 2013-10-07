from flask import Flask
from flask import request, render_template, redirect, url_for, session
from flask.ext import shelve

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
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        users = shelve.get_shelve()
        if users.has_key(username):
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
        users = shelve.get_shelve()
        if not users.has_key(username):
            return redirect(url_for("login"))
        elif users[username] != password:
            return redirect(url_for("login"))
        session["username"] = username
        return redirect(url_for("home"))

if __name__=="__main__":
    app.debug = True
    app.run()
