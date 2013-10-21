from flask import Flask
from flask.ext import shelve
from flask import session,url_for,request,redirect,render_template
import sqlite3
import utils 

app = Flask(__name__)
app.secret_key="mysecretkey"
app.config['SHELVE_FILENAME'] = 'my_users.db'
shelve.init_app(app)

@app.route("/")
def home():
    if 'count' in session:
        return redirect("/welcome")
    else:
        return redirect("/login")

@app.route("/count")
def count():
    try:
        c = session['count']
    except:
        c=0
    c=c+1
    session['count']=c
    page="""
    <h1>The count is: %d</h1>
    <a href="/count">count</a>
    """
    return page%(c)

@app.route("/welcome")
def welcome ():    
    return "<h1> Welcome to our website! </h1>"

@app.route("/login",methods=['GET','POST'])
def login():
    SQL_Users = sqlite3.connect ('SQL_Users')
    if request.method=="GET":
	return render_template("login.html")
    else:
	button = request.form['button']
	if button == 'Login':
            username = request.form['username'].encode ('ascii',"ignore")
	    password = request.form['password'].encode ('ascii',"ignore")
            if utils.authenticate(SQL_Users,username,password) == 1:
                session['username'] = username
                return redirect("/success")
            else:
                return redirect ("/login")
                print 'login attempt failed. Try again.'
	else:
	    return redirect("/register")
        
@app.route("/register",methods = ["GET","POST"])
def register():
    SQL_Users = sqlite3.connect ('SQL_Users')
    SQL_Users.execute ('CREATE TABLE if not exists users (username TEXT, password TEXT)')
    if request.method=="GET":
	return render_template("register.html")
    else:
	button = request.form['button']
	if button == "Submit":
	    username = request.form['username'].encode ('ascii',"ignore")
	    password = request.form['password'].encode ('ascii',"ignore")
            if utils.userNameExist (SQL_Users,username) == 0:
                utils.addUser (SQL_Users, username, password)
                print "Account Created"
                return redirect("/login")
            else:
                print "Username Taken, Try Again"
                return render_template("register.html")

@app.route("/success")
def success():
    session['count'] = 1
    return "<h1> You have successfully logged in!</h1>"

@app.route("/logout")
def logout():
    session.pop('count',None)
    return redirect(url_for('home'))

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
