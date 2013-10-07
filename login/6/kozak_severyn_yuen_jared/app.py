"""
app.py is a login engine.
"""

from flask import Flask
from flask import render_template
from flask import request, session, redirect, url_for

from flask.ext import shelve
from hashlib import sha512

app = Flask(__name__)

#conveniently convert a plaintext key to something convoluted
app.secret_key = sha512("cybersec").hexdigest()
app.config["SHELVE_FILENAME"] = "userData.db"
shelve.init_app(app)

@app.route("/")
def index():
	return render_template("index.html", loggedIn = "loggedIn" in session)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	Username = request.form["Username"].encode("ascii", "ignore")
	Password = request.form["Password"].encode("ascii", "ignore")
	users = shelve.get_shelve()

	if Username in users:
		if sha512(Password).hexdigest() == users[Username]:
			session["loggedIn"] = True
			return redirect(url_for("index"))
		return "Wrong credentials."
	return "No such user."

@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	users = shelve.get_shelve()
	Username = request.form["Username"].encode("ascii", "ignore")
	Password = request.form["Password"].encode("ascii", "ignore")
	PasswordRetype = request.form["PasswordRetype"].encode("ascii", "ignore")

	if Password != PasswordRetype:
		return "Password mismatch."

	if Username in users:
		return "Username already exists!"

	users[Username] = sha512(Password).hexdigest()
	return "Success."

@app.route("/vault")
def vault():
	return render_template("vault.html", loggedIn = "loggedIn" in session)

@app.route("/logout")
def logout():
	if "loggedIn" in session:
		session.pop("loggedIn")
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug = True)
