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

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"

@app.route("/login",methods=['GET', 'POST'])
def login():
  if request.method=="GET":
        return render_template("login.html")
        d={'username':request.form['username'],
           'password':request.form['password']}
        button=request.form['button']
        if button=="login":
            s="%(username)s:%(password)s\n"%(d)
            return redirect("/")
        else: 
            return render_template("login.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="GET":
        return render_template("form.html")
        d={'name':request.form['username'],
           'HR':request.form['HR']}
        button=request.form['button']
        if button=="Submit":
            s="%(name)s:%(HR)s\n"%(d)
            return redirect("/")
            return render_template("render_template.html",d=d)
        else:
            return redirect("/")
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
