from flask import Flask, session, redirect, request, url_for, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'database.db'
app.secret_key = "secret key"
shelve.init_app(app)

@app.route("/")
@app.route("/home")
def home():
    if 'user' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('login'))
 
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
                      
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("register.html", message = "")
    else:
        button = request.form['button'].encode("utf8")
        if button == "Register":
            user = request.form['user'].encode("utf8")
            pw = request.form['pass'].encode("utf8")
            data = shelve.get_shelve()
            if user in data:
                return render_template("register.html", message = "User exists already. Please login")
            else:
                data[user] = pw
                session['user'] = user
                return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        user = request.form['user'].encode("utf8")
        pw = request.form['pass'].encode("utf8")
        data = shelve.get_shelve()
        if user == "" or pw == "":
            return render_template("login.html", message = "Please enter your username and password.") 
        elif user not in data:
            return render_template("login.html", message = "User does not exist. Please sign up.")
        elif data[user] == pw:
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template("login.html", message = "Invalid username and password combination. Usernames and passwords are case sensitive. Please try again.")

if __name__ == "__main__":
    app.debug = True
    app.run()
