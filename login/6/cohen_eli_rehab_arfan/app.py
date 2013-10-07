from flask import Flask
from flask import request, render_template, redirect, session, url_for
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)
app.secret_key = "my secret key"


@app.route("/")
def home():
    if "username" in sesson:
        return render_template("home.html")
    else:
        return redirect("/login")

    
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html") 
    else:
        data = shelve.get_shelve()
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        
        if username in data:
            return "Username exists in the database!"        
        else:
            data[username] = password
            session["username"] = username
            return redirect("/login", errormessage = "<h1>Congrats! You have successfully registered!</h1>")

        
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html", errormessage="<h1>HI!</h1>")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        data = shelve.get_shelve()
        if not username in data:
            return redirect("/login", errormessage="<h1>Username does not exist!</h1>")
        elif data[username] != password: 
            return redirect("/login", errormessage="<h1>Username does not match password.</h1>")
        session["username"] = username
        return redirect("/")

    
@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect("/")


if __name__ = "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
