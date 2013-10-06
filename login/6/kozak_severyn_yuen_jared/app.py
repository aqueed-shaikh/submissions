"""
app.py is a login engine.
"""

from flask import Flask
from flask import render_template, request
import shelve

app = Flask(__name__)

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

		#still debugging
		data = shelve.open("appData")
		data[Username] = Password
		data.close()
		return "Success."

@app.route("/register", methods = ["GET", "POST"])

def register():
	if request.method == "GET":
		return render_template("register.html")
	#else:


#@app.route("/vault")
#def vault():

if __name__ == "__main__":
	app.run(debug = True)
