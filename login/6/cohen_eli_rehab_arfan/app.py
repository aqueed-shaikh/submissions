from flask import Flask
from flask import request, render_template, redirect, session, url_for
import utils

app = Flask(__name__)
app.secret_key = "abcd"

@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html")
    else:
        return redirect("/login")

    
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html") 
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        if (utils.addUser(username, password)):
            session["username"] = username
            return redirect("/login")
        else:
            return redirect("/register")
        
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        if (utils.checkUser(username, password)):
            return redirect("/")
        else:
            return redirect("/register")

    
@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect("/")

@app.route("/pi")
def pi():
    if "username" in session:
        return """
<h1>FIRST 3 DIGITS OF PI!!!!!!!!!!!</h1>
 
3.14
"""
    else:
        return redirect("/login")


if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
