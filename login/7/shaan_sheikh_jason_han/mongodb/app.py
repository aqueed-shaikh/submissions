from flask import Flask
from flask import request, render_template, url_for, redirect, session, flash
import cgi
import shelve
from auth import *

app = Flask(__name__)
app.secret_key ='my secret key'

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('loggedin'))
    else:
        return redirect(url_for('login'))

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
       # if valid_login(request.form["id"],
                      # request.form["pw"]):
        #form = cgi.FieldStorage()
        #if "Button1" in form:
        ID = request.form['id'].encode('ascii','ignore')
        PW = request.form['pw'].encode('ascii','ignore')
        a = authenticate(ID,PW)
        if a == -2:
            flash("Username is not registered in database. Redirecting to Register Page")
            return redirect(url_for('register'))
        elif a == -1:
            flash("Username and Password do not match.")
            return redirect(url_for('login'))
        else:
            session["username"] = ID
            return redirect(url_for("loggedin"))
    else:
        return render_template("login.html")


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        ID = request.form['id'].encode('ascii','ignore')
        PW = request.form['pw'].encode('ascii','ignore')
        a = add_user(ID,PW)
        if a == -1:
            return redirect(url_for('register'))
        else:
            session["username"] = ID
            return redirect(url_for('loggedin'))
    return render_template("register.html")
        

@app.route("/loggedin", methods = ["GET","POST"])
def loggedin():
    if "username" in session:
        if request.method == "POST":
            return redirect(url_for('logout'))
    return render_template("loggedin.html")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
        
    
if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
