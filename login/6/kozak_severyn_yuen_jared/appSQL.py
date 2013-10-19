from flask import Flask
from flask import render_template, url_for, redirect
from flask import request, session
import sqlite3

app = Flask(__name__)
app.secret_key = "trillest"

@app.route("/")
def index():
	return render_template("index.html", loggedIn = "loggedIn" in session)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	username = request.form["username"].encode("ascii", "ignore")
	password = request.form["password"].encode("ascii", "ignore")
	conn = sqlite3.connect("userData.sql")
	realPasswd = conn.cursor().execute("SELECT password FROM users WHERE username = ?", (username,)).fetchone()[0]

	if password == realPasswd:
		session["loggedIn"] = True
		return redirect(url_for("index"))
	else:
		return "Login failed."

@app.route("/logout")
def logout():
	session.pop("loggedIn")
	return redirect(url_for("index"))

@app.route("/register", methods = ["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	username = request.form["username"]
	password = request.form["username"]
	passwordRetype = request.form["passwordRetype"]

	conn = sqlite3.connect("userData.sql")
	if password == passwordRetype:
		conn.cursor().execute("INSERT INTO users values('Trill', 'Son', ?, ?)", (username, password,))
		conn.commit()
		return redirect(url_for("index"))
	else:
		return "Password mismatch."

@app.route("/vault")
def vault():
	return render_template("vault.html", loggedIn = "loggedIn" in session)

if __name__ == "__main__":
	app.run(debug = True)
