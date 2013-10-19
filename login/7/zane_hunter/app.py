from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
import sqlite3
import login

app = Flask(__name__)
app.secret_key = login.secret_key

#set up table if it doesn't exist
conn = sqlite3.connect(login.userdata_filename)
command = 'create table if not exists users (name text, password text)'
conn.cursor().execute(command)
conn.commit()
conn.close()


@app.route('/')
def home():
	if 'uname' in session: 
		return render_template("ferns.html",name=session['uname'])

	return render_template("index.html")


@app.route('/wittle')
def wittle():
	if 'uname' in session:
		return render_template('wittle.html')

	redirect(url_for('home'))


@app.route('/register', methods=["POST", "GET"])
def register():
	if request.method == "GET":
		return render_template("register-form.html")

	#post
	form = request.form
	if not form['button']:
		return render_template("register-form.html", d=form,
							   failure=False)

	#register
	passWorks = form['password'] == form['passconfirm']
	registered = False
	if passWorks:
		registered = login.registerUser(form['username'], form['password'])

	#registration success
	if passWorks and registered:
		return render_template("register-success.html", d=form)

	#registration failure
	return render_template("register-form.html", d=form, failure=True)


@app.route('/login',methods=["GET","POST"])
def signIn():
	if request.method == "POST": #post
		data = request.form
		if login.checkUser(app,data["uname"],data["passw"]):
			session['uname'] = data["uname"]
			return redirect(url_for('home'))
		else:
			return render_template("whoops.html")
	else:#get
		return render_template("login.html")


@app.route('/change-password', methods=["GET", "POST"])
def changePassword():
	if request.method == "GET":
		return render_template('change-password-form.html')

	#POST
	form = request.form

	return render_template('change-password-success.html')


@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
