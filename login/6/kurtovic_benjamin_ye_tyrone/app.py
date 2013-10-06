# Benjamin Kurtovic and Tyrone Ye

from flask import Flask
from flask import Flask, session, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config["SHELVE_FILENAME"] = "login.db"
app.secret_key = "Ben_Tyrone_L0G!N"
shelve.init_app(app)

def read_login(request):
    return (request.form["username"].encode("utf8"),
            request.form["password"].encode("utf8"))

def fail(template, error):
    return render_template(template + ".html", error=error)

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username, password = read_login(request)
    if not username or not password:
        return fail("login", "missing")
    db = shelve.get_shelve()
    if username.lower() not in db:
        return fail("login", "no-user")
    if db[username.lower()] != password:
        return fail("login", "incorrect")
    session["username"] = username
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    username, password = read_login(request)
    if not username or not password:
        return fail("register", "missing")
    db = shelve.get_shelve()
    if username.lower() in db:
        return fail("register", "exists")
    db[username.lower()] = password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
