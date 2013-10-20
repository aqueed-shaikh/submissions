from flask import Flask
from flask import session, url_for, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.secret_key="marlyandme"
app.config['SHELVE_FILENAME'] = 'username.db'
shelve.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if "username" in session:
        return render_template("index.html",username=session["username"])
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        users = shelve.get_shelve()
        if not users.has_key(username):
            return redirect(url_for("register"))
        if users[username] != password:
            return redirect(url_for("login"))
        session["username"] = username
        return redirect("/home")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"].encode("ascii", "ignore")
        password = request.form["password"].encode("ascii", "ignore")
        users = shelve.get_shelve()
        if users.has_key(username):
            return render_template("register.html")
        users[username] = password
        session["username"] = username
        return redirect(url_for("home"))
                    
@app.route("/reset", methods = ['GET', 'POST'])
def reset():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)
