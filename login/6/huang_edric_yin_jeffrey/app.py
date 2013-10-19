from flask import Flask
from flask import render_template, url_for, redirect, session, request
#SQL Changes
import urllib
import utils
app = Flask(__name__)
app.secret_key="mysecretkey"
#app.config['SHELVE_FILENAME'] = 'shelve.db'
#shelve.init_app(app)

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
        x = utils.authenticate(Username,Password)
        if x== 1:
            return redirect("/login?error="+"1")
        elif x==2:
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
        x = utils.register(username, password)
        if x == 0:
            return render_template("register.html",error="Username must be at least 4 characters.")
        if x == 1:
            return render_template("register.html",error="Password must be at least 6 characters.")
        if x == 2:
            return render_template("register.html",error="This username already exists.")
        session["username"] = username
        return redirect("/")

@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop("username",None)
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)

