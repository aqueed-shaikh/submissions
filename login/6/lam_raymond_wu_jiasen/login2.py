from flask import Flask, request, render_template, redirect, session, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('data.db')

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
		name = request.form['username']
		pw = request.form['password']
		if other.verify(name,pw):
			session['username'] = name
			redirect(url_for('hidden.html'))
		else:
			return render_template("login.html", message = "Invalid Username or Password")


@app.route("/register", methods = ['GET', 'POST'])
def register():
	if request.method=="GET":
		return render_template("register.html")
	else:
		name = request.form['username']
		pw = request.form['password']	
		if other.checkcopy(name):
			other.add(name,pw)
			return redirect(url_for('about'))
		else:
			return render_template("register.html", message = "Username Taken")

@app.route("/logout")
def logout():
	session.pop('count', None)
	return render_template("login.html", message = "Welcome!")

if __name__=="__main__":
    app.debug=True
    app.run()
