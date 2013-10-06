from flask import Flask, session, redirect, request, url_for, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)
app.secret_key='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username'].encode('ascii', 'ignore')
        password = request.form['password'].encode('ascii', 'ignore')
        database = shelve.get_shelve()
        if username not in database:
            return redirect(url_for('register', message='Not a valid username. Please register'))
        elif database[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Please check your username and password again')

@app.route('/register', methods = ['GET','POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    elif request.method == 'GET':
        if 'message' in request.args:
          return render_template('register.html', message=request.args['message'])
        return render_template('register.html')
    else:
        username = request.form['username'].encode('ascii', 'ignore')
        password = request.form['password'].encode('ascii', 'ignore')
        database = shelve.get_shelve()
        if username in database:
            return render_template('register.html', message='Username already in use')
        else:
            database[username] = password
            session['username'] = username
            return redirect(url_for('home'))

        
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
