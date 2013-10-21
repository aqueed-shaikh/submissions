# Login Assignment
# Josua Chin and Sabrina Khan
# October 6, 2013

from flask import Flask
from flask import redirect
from flask import url_for
from flask import session
from flask import request
from flask import render_template
#from flask.ext import shelve
import auth
#import sqlite3
from pymongo import MongoClient

app = Flask(__name__)
#app.config["SHELVE_FILENAME"] = "shelve.db"
#shelve.init_app(app)
app.secret_key = "key"

client = MongoClient()
db = client.db
users = db.users

@app.route("/")
def Home():
     if "Username" in session:
          return render_template("Home.html")
     else:
          return redirect(url_for("Login"))

@app.route("/Login",methods = ["POST", "GET"])
def Login():
     if "Username" in session:
          return redirect(url_for("Home"))
     elif request.method == "GET":
          return render_template("Login.html")
     elif request.method == 'POST':
          User = request.form['Username']
          if auth.authenticate(User, request.form['Password']):
               session['Username'] = User
               return render_template("Home.html")
          else:
               return render_template("Login.html") 
          #Username = request.form["Username"].encode("ascii","ignore")
          #Password = request.form["Password"].encode("ascii","ignore")
          #Database = shelve.get_shelve()
          #if Username not in Database:
           #    return redirect(url_for("Register"))
          #elif Database[Username] == Password:
           #    session["Username"] = Username
            #   return redirect(url_for("Home"))
          #else: 
           #    return render_template("Register.html")

@app.route("/Register", methods=['GET','POST'])
def Register():
     if "Username" in session:
          return redirect(url_for("Home"))
     elif request.method == "GET":
          return render_template("Register.html")
     elif request.method == "POST":
          User = request.form["Username"]
          if not auth.authenticate(User, request.form['Password']):
               auth.adduser(User, request.form["Password"])
               session["Username"] = User
          #Database = shelve.get_shelve()
          #if Username in Database:
          #     return render_template("Register.html")
          #else:
          #     Database[Username] = Password
              
          return redirect(url_for("Home"))

@app.route("/Logout")
def Logout():
     session.pop("Username",None)
     return redirect(url_for("Home"))

if __name__== "__main__":
    app.debug = True;
    app.run(host="0.0.0.0", port = 5005)
