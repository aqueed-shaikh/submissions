#Zhu Julie, Jason Zhen

from flask import Flask
from flask import session, url_for, request, redirect, render_template

app= Flask(__name__)
app.debug-True
app.secret_key="sekrit"
import auth

@app.route("/")
def index():
    #if ("username" in session):
    #return render_template("index.html",username=session["username"])
    #else:
    return redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
    if (request.method=="GET"):
        return render_template("login.html")

    Username=request.form["Username"].encode("ascii","ignore")
    Password=request.form["Password"].encode("ascii","ignore")

@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method=="GET"):
        return render_template("register.html")
    
