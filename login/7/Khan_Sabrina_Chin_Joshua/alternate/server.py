import os
from flask import Flask, session, redirect, url_for, escape, request, render_template
from database import Database

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = Database(app, 'users.dat')


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html',username=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = db.find_user(username)
        if users is not None and password == users.password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login_error.html') 
            

@app.route('/register', methods = ['POST', 'GET'])    
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not db.is_user(username):
            db.register(username, password)
            return redirect(url_for('login'))
        else:
            return render_template('registration_error.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run(host='0.0.0.0',port=5000)
