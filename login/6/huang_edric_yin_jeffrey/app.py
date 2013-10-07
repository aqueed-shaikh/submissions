from flask import Flask
from flask import render_template, url_for, redirect, session, request
from flask.ext import shelve

app = Flask(__name__)
app.secret_key="mysecretkey"
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)

@app.route("/")
def home(): 
    if "username" in session:
        return render_template("home.html",username=session["username"])
    else:
        return redirect("/login",errormessage="<p>Hello there!</p>")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html",errormessage="<p>Hello there!</p>")
    else:
        Username = request.form["username"].encode("ascii","ignore")
        Password = request.form["password"].encode("ascii","ignore")
        users = shelve.get_shelve()
        if not users.has_key(Username):
            return redirect("/login",errormessage="<p>Username does not exist. Try again.</p>")
        elif users[Username] != Password: 
            return redirect("/login",errormessage="<p>Username does not match password. Try again.</p>")
        session["username"] = Username
        return redirect("/")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html",error="Hello there!")
    else:
        Username = request.form["username"].encode("ascii","ignore")
        Password = request.form["password"].encode("ascii","ignore")
        users = shelve.get_shelve()
        if users.has_key(username):
            return redirect("/register",error="This username already exists.")
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
