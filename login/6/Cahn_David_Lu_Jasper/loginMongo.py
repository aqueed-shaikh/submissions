from flask import Flask
from flask.ext import shelve
from flask import session,url_for,request,redirect,render_template
from pymongo import MongoClient
import utils

app = Flask(__name__)
app.secret_key = 'hi'
blah = MongoClient()
db = blah.test

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="GET":
	return render_template("login.html")
    else:
	button = request.form['button']
	if button == 'Login':
            username = request.form['username'].encode ('ascii',"ignore")
	    password = request.form['password'].encode ('ascii',"ignore")
            if utils.auth(username,password,db.login):
                session['username'] = username
                return redirect("/success")
            else:
                return redirect ("/login")
                print 'login attempt failed. Try again.'
	else:
	    return redirect("/register")
        
@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method=="GET":
	return render_template("register.html")
    else:
	button = request.form['button']
	if button == "Submit":
	    username = request.form['username'].encode ('ascii',"ignore")
	    password = request.form['password'].encode ('ascii',"ignore")
            if not utils.auth(username,password,db.login):
		utils.addUser(username,password,db.login)
                print "Account Created"
                return redirect("/login")
            else:
                print "Username Taken, Try Again"
                return render_template("register.html")

@app.route("/success")
def success():
    return "<h1> You have successfully logged in!</h1>"

@app.route("/logout")
def logout():
    return redirect(url_for('home'))

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
