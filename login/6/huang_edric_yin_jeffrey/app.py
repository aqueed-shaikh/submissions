from flask import Flask
from flask import render_template, url_for, redirect, session, request
from flask.ext import shelve

import urllib
app = Flask(__name__)
app.secret_key="mysecretkey"
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)

@app.route("/")
def home(): 
    if "username" in session:
        return render_template("home.html",username=session["username"])
    else:
        return redirect("/login?errormessage="+"0")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        error = request.args.get("error")
        if error != None:
            if error == "0":
                errormessage= "You are not logged in! Login first to access our exclusive site features!"            
            elif error == "1":
                errormessage = "Username does not exist. Try again."
            else:
                errormessage = "Username does not match password."
                if session['loginattempts'] > 3:
                    errormessage = "Login attempts exceeded. This incident will be reported."
            return render_template("login.html",errormessage=errormessage)
        else: 
            return render_template("login.html")
    else:
        Username = request.form["username"].encode("ascii","ignore")
        Password = request.form["password"].encode("ascii","ignore")
        users = shelve.get_shelve()
        if not users.has_key(Username):
            return redirect("/login?error="+"1")
        elif users[Username] != Password:
            try:
                c = session['loginattempts']
            except:
                c = 0
            c = c + 1
            session["loginattempts"]=c
            return redirect("/login?error="+"2")
        session["username"] = Username
        session.pop('loginattempts',None)
        return redirect("/")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.form['button'] == "Cancel":
        return redirect(url_for('login'))
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        users = shelve.get_shelve()
        if users.has_key(username):
            return render_template("register.html",error="This username already exists.")
        if len(username) < 4:
            return render_template("register.html",error="Username must be at least 4 characters.")
        if len(password) < 6:
            return render_template("register.html",error="Password must be at least 6 characters.")

            
        users[username] = password
        session["username"] = username
        return redirect("/")

@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop("username",None)
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
