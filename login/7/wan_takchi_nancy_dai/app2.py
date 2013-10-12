from flask import Flask, session, redirect, request, url_for, render_template
import auth

app2 = Flask(__name__)

@app2.route("/")
@app2.route("/home")
def home():
    if 'user' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('login'))

@app2.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app2.route("/register", methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("register.html", message = "")
    else:
        button = request.form['button'].encode("utf8")
        if button == "Register":
            if auth.adduser(request.form['user'], request.form['pass']) == True:
                return redirect(url_for('home'))
            else:
                return render_template("register.html", message = "User exists already. Please login.")
        else:
            return redirect(url_for('login'))

@app2.route("/login", methods = ['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        user = request.form['user']
        pw = request.form['pass']
        if user == "" or pw == "":
            return render_template("login.html", message = "Please enter your username and password.")
        elif auth.authenticate(user, pw) == True:
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template("login.html", message = "Invalid username and password combination. Usernames and passwords are case sensitive. Please try again.")
        
if __name__ == "__main__":
    app2.debug = True
    app2.run(host = "0.0.0.0", port = 5005)
