from flask import Flask, session, redirect, request, url_for, render_template
import auth2

app3 = Flask(__name__)
app3.secret_key = "secret key"

@app3.route("/")
@app3.route("/home")
def home():
    if 'user' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('login'))

@app3.route("/account", methods = ['GET', 'POST'])
def account():
    if request.form['button'].encode("utf8") == "Save":
        if auth2.changePass( == True:
            return render_template("account.html", message = "Success")
        else:
            return render_template("account.html", message = "Incorrect old password.")
    else:
        return render_template("account.html", message = "")

@app3.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app3.route("/register", methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("register.html", message = "")
    else:
        button = request.form['button'].encode("utf8")
        if button == "Register":
            if auth2.register(request.form['user'], request.form['pass']) == True:
                return redirect(url_for('home'))
            else:
                return render_template("register.html", message = "User exists already. Please login.")
        else:
            return redirect(url_for('login'))

@app3.route("/login", methods = ['GET', 'POST'])
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
        elif auth2.login(user, pw) == True:
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template("login.html", message = "Invalid username and password combination. Usernames and passwords are case sensitive. Please try again.")

if __name__ == "__main__":
    app3.debug = True
    app3.run(host = "0.0.0.0", port = 5005)
