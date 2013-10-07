1#!/usr/bin/python
#!flask/bin/python

#This is Jack Cahn and Alvin Leung's Project

from flask import Flask
from flask import url_for,render_template
from flask import session,request,redirect
from flask.ext import shelve



app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'my_users.db'
app.secret_key="secret_key"
shelve.init_app(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/sign_in",methods=['GET','POST'])
def sign_in():
    pass

@app.route("/register",methods=['GET','POST'])
def register():
    my_users = shelve.get_shelve('c')
    if request.method == 'GET':
        return render_template("register.html",error="")
    elif request.method == 'POST':
        user = request.form['user'].encode('ascii','ignore')
        pw = request.form['pass'].encode('ascii','ignore')
        if my_users.haskey(user):
            return render_template("register.html",error="Username already exists")
        else:
            userdb[user] = pw
            return redirect(url_for('home')) #Change to sign_in when sign in works

if __name__ == "__main__":
    app.debug = True
    app.run()
