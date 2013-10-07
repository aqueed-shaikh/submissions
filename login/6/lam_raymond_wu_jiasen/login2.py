from flask import Flask, request, render_template, redirect, session, url_for
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'users.db'
app.secret_key='my secret key'
shelve.init_app(app)


@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"

@app.route("/hidden")
def hidden():
    if 'username' in session:
        return "<h1> in the secret page </h1>"
    else:
        return redirect(url_for('login'))

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method=="GET":
		return render_template("login.html", message = "")
    else:
		db = shelve.get_shelve()
		name1 = request.form['username']
		pw1 = request.form['password']
		name2 = name1.encode('ascii','ignore')
		pw2 = pw1.encode('ascii','ignore')
		if (db.has_key(name2) and db[name2]==pw2):
			session['username'] = name2
			redirect(url_for('hidden.html'))
		else:
			return render_template("login.html", message = "Invalid Username or Password")

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if request.method=="GET":
		return render_template("register.html")
	else:
		db = shelve.get_shelve()
		name1 = request.form['username']
		pw1 = request.form['password']
		pw2 = pw1.encode('ascii','ignore')
		name2 = name1.encode('ascii','ignore')
		if (name1 in 'people'):
			return render_template("register.html", message = "Username Taken")
		else:
			db[name2] = pw2
			session['username'] = name2
			return redirect(url_for('about'))

@app.route("/logout")
def logout():
	session.pop('count', None)
	return render_template("login.html", message = "Welcome!")

if __name__=="__main__":
    app.debug=True
    app.run()
