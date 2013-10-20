# Will Field-Thompson & Haoxin Luo

import auth
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
#def auth.authenticate(u, p):
#    db = get_shelve()
#    return u in db and db[u] == p

#need a more interesting homepage
@app.route('/')
def home():
    if 'username' in session:
        return render_template("home.html", user=session['username'])
    return redirect("/login")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user = request.form['username']
        if not auth.add_user(user, request.form['password']): 
            return "Username already in use. Please pick another." + render_template('register.html')
        else:
            session['username'] = user
            return redirect('/registered')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form['username']
        if auth.authenticate(user, request.form['password']):
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
        return render_template('registered.html', user=session['username'])
    return redirect("/")

@app.route('/setpass', methods=['POST', 'GET'])
def setpass():
    if 'username' in session:
        if request.method == 'GET':
            return render_template('setpass.html', user=session['username'])
        elif request.method == 'POST':
            auth.set_pass(session['username'], request.form['password'])
    else:
        return redirect('/')
    

#content

@app.route('/procrastination')
def procrastination():
    if 'username' in session:
        return render_template('procrastination.html', user=session['username'])
    return redirect("/")

@app.route('/work')
def work():
    if 'username' in session:
        return render_template('work.html', user=session['username'])
    return redirect("/")

@app.route('/future')
def future():
    if 'username' in session:
        return render_template('future.html', user=session['username'])
    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
