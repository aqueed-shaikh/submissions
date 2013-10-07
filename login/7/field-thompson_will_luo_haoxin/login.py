# Will Field-Thompson & Haoxin Luo

# To do:
# Add a register link to the login page
# Add other pages
# Add new homepage

from flask import Flask
import flask.ext.shelve
from flask.ext.shelve import get_shelve, init_app
from flask import render_template, session, request, redirect

app = flask.Flask(__name__)
# Configuring shelve:
app.config['SHELVE_FILENAME'] = 'users.dat'
app.config['SHELVE_WRITEBACK'] = True
app.secret_key = 'HEREISAVERYSECRETKEY'

init_app(app)

# How logins are stored (currently):
# shelve database has usernames for keys
# stored under each username is the password

# checks username against password
def verify_login(u, p):
    db = get_shelve()
    return u in db and db[u] == p

#need a more interesting homepage
@app.route('/')
def home():
    if 'username' in session:
        return render_template("home.html")
#        return '<h1>Hi %s!</h1>'%session['username']
    return redirect("/login")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user = request.form['username'].encode("ascii")
        db = get_shelve()
        if user in db: #checks to make sure the username doesn't already exist
            return "Username already in use. Please pick another." + render_template('register.html')
        else:
            db[user] = request.form['password'].encode("ascii")
            session['username'] = user
            return redirect('/registered')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form['username'].encode("ascii")
        if verify_login(user, request.form['password'].encode("ascii")):
            session['username'] = user
            return redirect('/')
        else:
            return "<h2>Password/Login mismatch</h2>"


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


#just something that tells the user that they have successfully registered
@app.route('/registered')
def registered():
    if 'username' in session:
        return render_template('registered.html')
    return redirect("/")


@app.route('/procrastination')
def procrastination():
    if 'username' in session:
        return render_template('procrastination.html')
    return redirect("/")

@app.route('/work')
def work():
    if 'username' in session:
        return render_template('work.html')
    return redirect("/")

@app.route('/future')
def future():
    if 'username' in session:
        return render_template('future.html')
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
