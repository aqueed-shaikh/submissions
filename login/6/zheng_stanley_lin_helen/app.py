from flask import Flask
from flask import request, render_template, redirect, url_for, session
from pymongo import MongoClient
connection = MongoClient()
import sqlite3
import auths

app = Flask(__name__)
app.secret_key="my secret key"


#DEFAULT
@app.route("/")
def default():
    return redirect("/home")

@app.route("/home")
def home():
    if 'user' in session:
        return render_template('home.html')
    else:
        return redirect("/login")



#LOGIN PAGE    
@app.route("/login",methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if auths.check(username, password):
            session["user"] = username
            return redirect(url_for("login"))
        else:
            return redirect(url_for("home"))
    


#REGISTER
@app.route("/register",methods = ['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html", message = "Type in desired username and password")
    else:
       username = request.form["username"]
       password = request.form["password"]
       if auths.usernameExists(username):
           return render_template("register.html", message = "Username exists already")
       else:
           auths.add(username, password)
           return redirect(url_for("home"))


#CHANGE PASSWORD
@app.route("/change",methods = ['GET','POST'])
def change():
    if request.method == "GET":
        return render_template("changepass.html", message = "Type in username, current password, and new password")
    else:
        username = request.form["username"]
        password = request.form["currentPassword"]
        newPassword1 = request.form["newPassword1"]
        newPassword2 = request.form["newPassword2"]
        if auths.check(username, password):
            if newPassword1==newPassword2:
                auths.changePass(username, password, newPassword1)
                return redirect("/home")
        else:
            return redirect("/change", message = "username and password do not match or new password does not match")


#POP THE USERNAME
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user',None)
    return redirect("/home")


if __name__=="__main__":
    app.debug=True
    auths.start()
    app.run(host='0.0.0.0', port=5000)
