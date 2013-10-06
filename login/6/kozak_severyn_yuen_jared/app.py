"""
app.py is a login engine.

"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def index():
	return render_template("index.html")

	
@app.route("/login", methods = ["GET", "POST"])

def login():
	if request.method == "GET":
		return render_template("login.html")


@app.route("/register", methods = ["GET", "POST"])

def register():
	if request.method == "GET":
		return render_template("register.html")
	else:


#@app.route("/vault")
#def vault():

if __name__ == "__main__":
	app.run(debug = True)
