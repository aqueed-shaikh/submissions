#Made by Simon Chen and Derek Tang
from flask import Flask
from flask import session, url_for, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'accounts.db'
app.secret_key = "as124fa6s3426joijtoq124wm10525e"
shelve.init_app(app)


@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET" :
        return render_template("login.html")
    else:
        username = request.form["username"].encode("ascii","ignore")
        password = request.form["password"].encode("ascii", "ignore")
        button = request.form['button']
        accounts = shelve.get_shelve()
        if button == "Login":
            if username not in accounts:
                return redirect("/members")
            elif accounts[username] == password:
                session["username"] = username
                return redirect("/members")
            else:
                 return render_template("login.html")
        elif button == "Cancel":
            return render_template("login.html")
        
        
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET" :
        return render_template("register.html")
    else:
        username = request.form['username'].encode("ascii","ignore")
        password = request.form['password'].encode("ascii","ignore")
        confirmpassword = request.form['confirmpassword'].encode("ascii","ignore")
        accounts = shelve.get_shelve()
        button = request.form['button']
        if button == "Submit":
            if accounts.has_key(username):
                return render_template("register.html", message = "There is already an account under your name.")
            elif password != confirmpassword:
                return render_template("register.html", message = "Please correctly confirm your passwords.")
            else:
                accounts[username] = password
                session['username'] = username
                return redirect("/")
        elif button == "Cancel":
            return render_template("register.html")

@app.route("/members")
def members():
    if 'username' in session:
        return render_template("members.html", d = session)
        return page
    else:
        return redirect("/unknown")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")
    
@app.route("/unknown")
def unknown():
    page = """
    <h2> You need to login in</h2>
    <a href="/login">Login here!</a>
    <br>
    <a href="/register">Don't have an account?</a>
    """
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
