#Zhu Julie, Jason Zhen

from flask import Flask
from flask import session, url_for, request, redirect, render_template

app= Flask(__name__)
app.debug-True
app.secret_key="sekrit"
import auth

@app.route("/")
def index():
    if ("username" in session):
        return render_template("index.html",username=session["username"])
    else:
        return redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
    if (request.method=="GET"):
        return render_template("login.html")
    else:
        if auth.log(str(request.form["username"]),str(request.form["password"])):
            Username=request.form["Username"].encode("ascii","ignore")
            Password=request.form["Password"].encode("ascii","ignore")
            return redirect("/")

@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method=="GET"):
        return render_template("register.html")
    elif (request.form['button']=="Cancel"):
        return redirect("/login")
    else:
        if request.form["password"]==request.form["cpassword"]:
            if auth.addUser(str(request.form["username"]),str(request.form["password"]) ):
                return redirect("/login")

@app.route("/logout",methods=["GET","POST"])
def logout():
    session.pop("username",None)
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
