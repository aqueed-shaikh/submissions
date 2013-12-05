from flask import Flask
from flask import request, render_template, redirect, session, url_for
import utils

app = Flask(__name__)
app.secret_key = "abcd"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        if "username" in session:
            return render_template("home.html")
        else:
            return redirect("/login")
    else:
        password = request.form["password"].encode("ascii", "ignore")
        password2 = request.form["password2"].encode("ascii", "ignore")
       
        a = utils.changePwd(session["username"],password, password2)
        return render_template("home.html", error = a)


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html") 
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        password2 = request.form["password2"].encode("ascii", "ignore")
        a = utils.addUser(username, password, password2)
        if (a == "good"):
            return redirect("/login")
        else:
            return render_template("register.html", error = a)
        
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        if (utils.checkUser(username, password)):
            session["username"] = username
            return redirect("/")
        else:
            return redirect("/fail")


@app.route("/fail")
def fail():
    return """
<h1>Login failed</h1>

<a href="/login">Try again</a>   <a href="/register">Register</a>
"""

    
@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect("/")

@app.route("/pi")
def pi():
    if "username" in session:
        return render_template("pi.html")
    else:
        return redirect("/login")


@app.route("/windows")
def windows():
    if "username" in session:
        return render_template("windows.html")
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
