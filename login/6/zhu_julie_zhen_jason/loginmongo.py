#!/usr/bin/python

from flask import Flask
from flask import request, render_template, redirect, session, url_for, session
from authmongo import adduser, authenticate

app = Flask(__name__)
app.secret_key='secret key'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username'].encode('ascii','ignore')
        password = request.form['password'].encode('ascii','ignore')
        
    if authenticate(username, password):
        session['username'] = username
        return render_template("page.html")
    else:
        return redirect(url_for('login'))
          

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:

        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")

        if adduser(username, password):
            session['username'] = username
            return redirect(url_for('login'))
        else:
            return redirect(url_for('home'))


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
