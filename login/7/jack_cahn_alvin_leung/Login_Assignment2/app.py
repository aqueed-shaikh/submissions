#!/usr/bin/python
#!flask/bin/python

#This is Jack Cahn and Alvin Leung's Project

from flask import Flask
from flask import request
from flask import url_for,render_template
from flask import session,request,redirect
from flask.ext import shelve

app = Flask(__name__)
app.secret_key="secret_key"
app.config['SHELVE_FILENAME'] = 'my_users.db'
shelve.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "<h1>About</h1>"

@app.route("/login",methods=['GET', 'POST'])
def login():
    my_users = shelve.get_shelve('c')
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['button']
        if button == 'login':
            username = request.form['username'].encode ('ascii',"ignore")
            password = request.form['password'].encode ('ascii',"ignore")
            if username in my_users and my_users [username]["password"] == password:
                session['username'] = username
                return redirect("/form")
            else:
                return redirect("/login")
        else:
	    return redirect("/register")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        d={'name':request.form['username'],
           'HR':request.form['HR']}
        button=request.form['button']
        if button=="complete":
            f=open("data.dat","a")
            s="%(name)s:%(HR)s\n"%(d)
            f.write(s)
            f.close()
            return render_template("render_template.html",d=d)
        else:
            return redirect("/form")

@app.route("/register",methods=['GET','POST'])
def register():
    my_users = shelve.get_shelve('c')
    if request.method == 'GET':
        return render_template("register.html",error="")
    elif request.method == 'POST':
        user = request.form['user'].encode('ascii','ignore')
        pw = request.form['pass'].encode('ascii','ignore')
        if user in my_users:
            return render_template("register.html",error="Username already exists")
        else:
            my_users[user] = {"password":pw}
            return redirect(url_for('login')) #Change to sign_in when sign in works

@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)


