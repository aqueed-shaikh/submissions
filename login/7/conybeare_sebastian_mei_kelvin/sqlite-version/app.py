from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
import sqlite3
import login as lawgin

app = Flask(__name__)
app.secret_key = "cookies"

@app.route("/")
def home():
    return render_template ("index.html")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template ("login.html")
    else:
        usern = request.form['Username'].encode('ascii','ignore')
        passw = request.form['Password'].encode('ascii','ignore')
        if lawgin.login(usern,passw):
            session['Username'] = usern
            return redirect ("/success")
        else:
			return redirect ("/login")


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template ("register.html")
    else:
        usern = request.form["Username"].encode('ascii','ignore')
        passw = request.form["Password required"].encode('ascii','ignore')
        cpassw = request.form["Confirm Password"].encode('ascii','ignore')
	if cpassw == passw:
		if lawgin.register(usern,passw):
			return redirect ("/login")
		else:
			return redirect ("/error")
	else:
		return redirect ("/error")
@app.route("/success")
def sucess():
     return render_template ("LoginSuccess.html")

@app.route("/error")
def error():
    return render_template ("Error.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6969)
