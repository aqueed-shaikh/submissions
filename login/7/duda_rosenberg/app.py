#!/usr/bin/python

from flask import Flask
from flask import session, redirect, url_for, render_template, request
from pymongo import MongoClient



app = Flask(__name__)
#app.config['SHELVE_FILENAME'] = 'users.db'
#shelve.init_app(app)


client = MongoClient()
db = client.db
users = db.users


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
        user = str(request.form["usrnm"])
        pwd = str(request.form["psswrd"])
        #db = shelve.get_shelve("c")
        #info = connection.execute("select usernames.username, usernames.password from usernames where usernames.username == %s", usr);
        dbEntry = users.find({'username':user})
        usrn = dbEntry['username']
        pswd = dbEntry['password']
        #if db.has_key(user) and db[user] == pwd:
        if usrn == None:
            return  render_template("login.html", error="username or password not recognized")
        elif ((pwd != None) and (pswd == pwd)):
            return render_template("welcome.html",username=user, 
                                       message="How are you doing today?")
                                
        else:
            return  render_template("login.html", error="username or password not recognized")
        db.close()
    else:
        return render_template("login.html", error="")

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        usr = str(request.form['usr'])
        pwd = str(request.form['pwd'])
        
        if users.find({'username':usr}).count() != 0:
            return render_template('register.html',
                                   error = 'Username already exists')
        else:
            #db[usr] = pwd
            #db.close
            auth.addUser(usr, pwd);
            return render_template("welcome.html",username=usr)

            


if (__name__ == "__main__"):
    app.debug = True
    app.run(host = "0.0.0.0")
