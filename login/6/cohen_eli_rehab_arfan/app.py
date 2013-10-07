from flask import Flask
from flask import request, render_template, redirect, session, url_for
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)
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
        data = shelve.get_shelve()
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        
        if username in data:
            return "Username exists in the database!"        
        else:
            data[username] = password
            session["username"] = username
            return redirect("/login")

        
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii","ignore")
        data = shelve.get_shelve()
        if not username in data:
            return redirect("/register")
        elif data[username] != password: 
            return redirect("/register")
        session["username"] = username
        return redirect("/")

    
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

@app.route("/windows")
def windows():
    if "username" in session:
        return """
<h1>REASONS TO BUY WINDOWS 8:<h1>

"""
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
