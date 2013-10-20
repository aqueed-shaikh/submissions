"""

		appShelf.py is a login framework with python-shelf 
	integration which facilitates login, registration, and user 
	recognition (e.g. dynamically updating pages to reflect a 
	user's having successfully logged in).

"""

from flask import Flask
from flask import render_template
from flask import request, session, redirect, url_for

from flask.ext import shelve
from hashlib import sha512

app = Flask(__name__)

app.secret_key = sha512("cybersec").hexdigest() 	#conveniently convert a plaintext key to something convoluted
app.config["SHELVE_FILENAME"] = "userData.db"
shelve.init_app(app)

@app.route("/", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		session.pop("loggedIn")
	return render_template("index.html", loggedIn = "loggedIn" in session)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	username = request.form["username"].encode("ascii", "ignore")
	password = request.form["password"].encode("ascii", "ignore")
	users = shelve.get_shelve()

	if username in users:
		if sha512(password).hexdigest() == users[username]:
			session["loggedIn"] = True
			return redirect(url_for("index"))
		return "Wrong credentials."
	return "No such user."

@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	users = shelve.get_shelve()
	username = request.form["username"].encode("ascii", "ignore")
	password = request.form["password"].encode("ascii", "ignore")
	passwordRetype = request.form["passwordRetype"].encode("ascii", "ignore")

	if password != passwordRetype:
		return "password mismatch."

	if username in users:
		return "username already exists!"

	users[username] = sha512(password).hexdigest()
	return "Success."

@app.route("/vault")
def vault():
	return render_template("vault.html", loggedIn = "loggedIn" in session)

if __name__ == "__main__":
	app.run(debug = True)
