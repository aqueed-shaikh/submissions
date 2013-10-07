from flask import Flask, request, render_template, redirect, session, url_for
import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'users.db'
app.secret_key='my secret key'


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
		name1 = name.encode('ascii','ignore')
		pw1 = name.encode('ascii','ignore')
		people = shelve.open("sessions")
		if (people.has_key(name1) and people[name1]==pw1):
			people.close()
			session['username'] = name1
			redirect(url_for('hidden.html'))
		else:
			people.close()
			return render_template("login.html", message = "Invalid Username or Password")

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if request.method=="GET":
		return render_template("register.html")
	else:
		people = shelve.open("sessions")
		name1 = request.form['username']
		pw1 = request.form['password']
		pw2 = pw1.encode('ascii','ignore')
		name2 = name1.encode('ascii','ignore')
		if (name1 in 'people'):
			people.close()
			return render_template("register.html", message = "Username Taken")
		else:
			people[name2] = pw2
			people.close()
			session['username'] = name2
			return redirect(url_for('about'))

@app.route("/logout")
def logout():
	session.pop('count', None)
	return render_template("login.html", message = "Welcome!")

if __name__=="__main__":
    app.debug=True
    app.run()
    