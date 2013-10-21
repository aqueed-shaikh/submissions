from flask import Flask
from flask import request, render_template, redirect, url_for, session
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
