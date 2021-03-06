#!/usr/local/bin/python
from flask import Flask, session, redirect, request, url_for, render_template
import auth


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    return redirect(url_for('login'))


@app.route('/something')
def something():
    if 'username' in session:
        return render_template('something.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('login.html')
    username = request.form['username'].lower()
    password = request.form['password']
    if auth.authenticate(username, password):
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('login.html',
        message='Please check your username and password again')


@app.route('/change', methods=['GET', 'POST'])
def change():
    if request.method == 'GET':
        return render_template('change.html')
    username = session['username']
    oldpass = request.form['oldpass']
    newpass = request.form['newpass']
    cpass = request.form['cpass']
    if auth.authenticate(username, oldpass):
        if newpass == cpass:
            auth.change(username, newpass)
            return redirect(url_for('home'))
        return render_template('change.html',
            message='Passwords do not match')
    return render_template('change.html',
        message='Check old password again')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    elif request.method == 'GET':
        if 'message' in request.args:
            return render_template('register.html',
                message=request.args['message'])
        return render_template('register.html')
    username = request.form['username'].lower()
    password = request.form['password']
    cpass = request.form['cpass']
    if auth.exists(username):
        return render_template('register.html',
            message='Username already in use')
    if password == cpass:
        auth.insert(username, password)
        return redirect(url_for('home'))
    return render_template('register.html',
        message='Passwords do not match')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
