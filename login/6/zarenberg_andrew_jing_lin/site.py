
# Andrew Zarenberg
# Jing Lin
# SoftDev Period 6


from flask import Flask
from flask import render_template, session, redirect, url_for, request
from flask.ext import shelve
app = Flask(__name__)
app.debug = True
app.config['SHELVE_FILENAME'] = 'shelve.db'
app.secret_key = "Lin_Zarenberg_LOGIN"
shelve.init_app(app)
@app.route("/")
def index():
    if "username" in session: 
        return render_template("index.html", username=session["username"])
    else:
        return redirect(url_for("login"))
    
@app.route("/login", methods=["GET","POST"])
def login():
    d = shelve.get_shelve()
    if request.method == "POST":
        for n in d.keys():
            if n == str(request.form["username"]) and d[n] == request.form["password"]:
                session["username"] = request.form["username"]
                session["password"] = request.form["password"]
                return redirect(url_for("index"))
        return render_template("login.html",type=1)
    else:
        return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("index"))
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        if request.form["password"] == request.form["password2"]:
            d = shelve.get_shelve()
            for n in d.keys():
                if n == request.form["username"]:
                    return render_template("register.html",type=1)
            d[str(request.form["username"])] = request.form["password"]
            return redirect(url_for("login"))
    else:
        return render_template("register.html")
if __name__ == "__main__":
    app.run()
