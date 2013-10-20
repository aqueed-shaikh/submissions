# Will Field-Thompson & Haoxin Luo

import auth
from flask import Flask
from flask import render_template, session, request, redirect

app = Flask(__name__)

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
            if auth.authenticate(request.form['username'],request.form['password']):
                auth.set_pass(session['username'], request.form['npassword'])
            else:
                return "<h2> incorrect password </h2>"
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
