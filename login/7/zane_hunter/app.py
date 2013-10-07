from flask import Flask
from flask import render_template
from flask import request
from flask.ext import shelve
import login

app = Flask(__name__)

@app.route('/')
def home():
	return "<h3> Login </h3>"

@app.route('/register')
def register():
	
	
	return render_template("render.html")
@app.route('/login/',methods="GET,POST")
def login():
	if request.method == "POST": #post,get
		data = request.form
		if login.checkUser(app,data["uname"],data["passw"]):
			return render_template("logged.html")
		else:
			return render_template("whoops.html")
	else:
		return render_template("login.html")

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
