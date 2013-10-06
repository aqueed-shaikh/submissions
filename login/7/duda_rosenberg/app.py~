#!/usr/bin/python

from flask import Flask
from flask import session, redirect, url_for, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)

if (__name__ == '__main__'):
    app.debug = True
    app.run(host = '0.0.0.0')



@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render.template('login.html')
    elif shelve[username] == password:
        return redirect('/welcome')
    else:
        return render.template('login.html')


