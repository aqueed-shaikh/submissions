from flask import Flask, request, render_template, redirect, session, url_for
import verify

app = Flask(__name__)
app.secret_key="key"

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
                name = request.form["username"].encode("ascii", "ignore")
                pw = request.form["password"].encode("ascii", "ignore")
                if verify.verify(name,pw):
                        session['username'] = name
                        redirect(url_for('hidden'))
                else:
                        return render_template("login.html", message = "Invalid Username or Password")


@app.route("/register", methods = ['GET', 'POST'])
def register():
        if request.method=="GET":
                return render_template("register.html")
        else:
                name = request.form["username"].encode("ascii", "ignore")
                pw = request.form["password"].encode("ascii", "ignore")
                if verify.checkcopy(name):
                        verify.add(name,pw)
                        return redirect(url_for('about'))
                else:
                        return render_template("register.html", message = "Username Taken")

@app.route("/changepw", methods = ['GET', 'POST'])
def changepw():
	if request.method=="GET":
		return render_template("changepass.html")
	elif 'username' not in session:
		return redirect(url_for('login'))
	else:
		opw = request.form["oldpw"].encode("ascii", "ignore")
		npw = request.form["newpw"].encode("ascii" ,"ignore")
		cpw = request.form["cpw"].encode("adcii", "ignore")
		if npw == cpw:
			return redirect(url_for('about'))
		else:
			return render_template("changepass.html", message = "New PW and Confirm PW don't match.")

@app.route("/logout")
def logout():
        session.pop('count', None)
        return render_template("login.html", message = "Welcome!")

if __name__=="__main__":
    app.debug=True
    app.run()