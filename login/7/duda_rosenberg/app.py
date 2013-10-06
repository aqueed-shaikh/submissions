#!/usr/bin/python

from flask import Flask
from flask import session, redirect, url_for, render_template, request
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'users.db'
shelve.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', error="")
    elif request.method == "POST":
        #print "1"
        user = str(request.form["usrnm"])
        pwd = str(request.form["psswrd"])
        #print "2"
        db = shelve.get_shelve("c")
        #print "3"
        if db.has_key(user) && db[user] == pwd:
            return render_template("welcome.html",username=user, 
                                       message="How are you doing today?")
                                
        else:
            return  render_template("login.html",
                                    error="username or password not recognized")
        db.close()
        #print "6"
    else:
        #print "7"
        return render_template("login.html", error="")


if (__name__ == "__main__"):
    app.debug = True
    app.run(host = "0.0.0.0", port = 5005)
