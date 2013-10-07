from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
from flask.ext import shelve
import login

app = Flask(__name__)

app.secret_key = login.secret

app.config['SHELVE_FILENAME'] = "thea"
shelve.init_app(app)

@app.route('/')
def home():
	if 'uname' in session: 
		return render_template("ferns.html",name=session['uname'])
	else:
		return "<a href='/login/'><h3> Login </h3></a><a href='/register/'><h3>Register</h3></a>"

@app.route('/register', methods=["POST", "GET"])
def register():
	if request.method == "GET":
		return render_template("register-form.html")

	else: #post
		button = request.form['button']
		d = request.form
		if button == "Register":
			success = login.registerUser(d['username'], d['password'])

			if success:
				return render_template("register-success.html", d=d)
			else:
				return render_template("register-form.html", d=d, failure=True)
		else:
			return render_template("register-form.html", d=d, failure=False)

@app.route('/login/',methods=["GET","POST"])
def signin():
	if request.method == "POST": #post
		data = request.form
		if login.checkUser(app,data["uname"],data["passw"]):
			session['uname'] = data["uname"]
			return redirect(url_for('home'))
		else:
			return render_template("whoops.html")
	else:#get
		return render_template("login.html")
@app.route('/logout/')
def logout():
	session.clear()
	redirect_for("/")
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
