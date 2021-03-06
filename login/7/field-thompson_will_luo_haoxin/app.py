# Will Field-Thompson & Haoxin Luo

import auth
from flask import Flask
from flask import render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "SECRET KEY"

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
            return "<h2>Password/Login mismatch</h2>" + render_template("login.html")


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
            if auth.authenticate(session['username'],request.form['password']):
                if request.form['npassword'] == request.form['vpassword']:
                    auth.set_pass(session['username'], request.form['npassword'])
                    return redirect('/')
                else:
                    return "<h2>Passwords don't match</h2>" + render_template('setpass.html', user=session['username'])
            else:
                return "<h2> incorrect password </h2>" + render_template('setpass.html',user=session['username'])
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

@app.route('/test')
def test():
    return auth.test()

if __name__ == "__main__":
    app.debug = True
    app.run()
