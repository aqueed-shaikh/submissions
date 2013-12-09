"""

		appSQL.py is a login framework with MongoDB integration, 
	which facilitates login, registration, and user recognition
	(e.g. dynamically updating pages to reflect a user's having 
	successfully logged in).

"""

from flask import Flask
from flask import render_template, url_for, redirect
from flask import request, session

from pymongo import MongoClient
from hashlib import sha512

app = Flask(__name__)
app.secret_key = sha512("cybersec").hexdigest() 	#conveniently convert a plaintext key to something convoluted

client = MongoClient()
db = client["userDataMongo"]

@app.route("/", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		session.pop("loggedIn")
	return render_template("index.html", loggedIn = "loggedIn" in session)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		result = db.userDataMongo.find_one({"username": username})

		if result is not None and password == result["password"]:
			session["loggedIn"] = True
			return redirect(url_for("index"))
		else:
			return "Login failed."

@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	username = request.form["username"]
	password = request.form["password"]
	passwordRetype = request.form["passwordRetype"]

	result = db.userDataMongo.find_one({"username": username})

	if result is not None:
		return "Username taken."
	elif password == passwordRetype:
		db.userDataMongo.insert({"username": username, "password": password})
		return redirect(url_for("index"))
	else:
		return "Password mismatch."

@app.route("/vault")
def vault():
	return render_template("vault.html", loggedIn = "loggedIn" in session)

if __name__ == "__main__":
	app.run(debug = True)
