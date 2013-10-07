from flask import Flask
from flask import request
from flask import render_template
from flask import request
from flask.ext import shelve
import login

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = "thea"
shelve.init_app(app)

@app.route('/')
def home():
	return "<h3> Login </h3>"

@app.route('/register', methods=["POST", "GET"])
def register():
	if request.method == "GET":
		return render_template("register-form.html")

	else: #post
		button = request.form['button']
		d = request.form
		if button == "Register":
			shelf = shelve.get_shelve(shelfName);

			if d['username'] in shelf:
				shelf.close()
				return render_template("register-failure.html", d=d)

			else:
				shelf[d['username']] = d['password']
				shelf.close()

				return render_template("register-success.html", d=d)
		else:
			return render_template("register-form.html")

@app.route('/login/',methods=["GET","POST"])
def signin():
	if request.method == "POST": #post
		data = request.form
		if login.checkUser(app,data["uname"],data["passw"]):
			return render_template("logged.html")
		else:
			return render_template("whoops.html")
	else:#get
		return render_template("login.html")

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
