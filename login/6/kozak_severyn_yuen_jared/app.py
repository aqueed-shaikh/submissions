"""
app.py is a login engine.
"""

from flask import Flask
from flask import render_template
from flask import request, session, redirect, url_for
import shelve
import hashlib

app = Flask(__name__)

#conveniently convert a plaintext key to something convoluted
app.secret_key = hashlib.sha512("security").hexdigest()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		Username = request.form["Username"].encode("ascii", "ignore")
		Password = request.form["Password"].encode("ascii", "ignore")
		users = shelve.open("userData")

		if Username in users:
			if Password == users[Username]:
				session["loggedIn"] = True
				return redirect(url_for('vault'))
			else: 
				return "Wrong credentials."
		else: 
			return "No such user."
		users.close()

@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	else:
		users = shelve.open("userData")

		Username = request.form["Username"].encode("ascii", "ignore")
		Password = request.form["Password"].encode("ascii", "ignore")
		PasswordRetype = request.form["PasswordRetype"].encode("ascii", "ignore")

		if Password != PasswordRetype:
			return "Password mismatch."

		elif Username in users:
			return "Username already exists!"

		else:
			users[Username] = Password
			return "Success."

@app.route("/vault")
def vault():
	if session["loggedIn"]:
		return "42."
	else:
		return redirect(url_for('login'))

@app.route("/logout")
def logout():
	session.pop("loggedIn")

if __name__ == "__main__":
	app.run(debug = True)
