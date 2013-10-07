from flask import Flask, render_template, session, request, redirect, url_for, session
from flask.ext import shelve
import md5

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'puppies_super_awesome'
shelve.init_app(app)

app.secret_key = 'super_secret_key'


# TODO: Make this actually encrypt stuff with an algorithm that isn't easily crackable
def get_password_encrypted(password):
    return md5.new(password).digest()

@app.route('/')
def home():
    db = shelve.get_shelve('c')
    logged_in = False
    username = ''
    if 'username' in session:
        logged_in = True
        username = session['username']
    return render_template('home.html', logged_in=logged_in, username=username, everyone=str(db))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        db = shelve.get_shelve('c')
        if not request.form['username'] in db:
            db[request.form['username']] = get_password_encrypted(request.form['password'])
            return redirect(url_for('home'))
        else:
            message = "That username is taken!"
            return render_template('register.html', message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        db = shelve.get_shelve('c')
        if request.form['username'] in db:
            if db[request.form['username']] == get_password_encrypted(request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else:
                message = "Username or password not known"
                return render_template('login.html', message=message)
        else:
            message = "Username or password not known"
            return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/friends')
def friends():
    if 'username' in session:
        return render_template('friends.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
