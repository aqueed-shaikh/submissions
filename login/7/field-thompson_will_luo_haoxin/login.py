# Will Field-Thompson & Haoxin Luo

from flask import Flask
import flask.ext.shelve
from flask.ext.shelve import init_app
from flask import render_template

app = flask.Flask(__name__)
# Configuring shelve:
app.config['SHELVE_FILENAME'] = 'users.dat'
app.config['SHELVE_WRITEBACK'] = True

init_app(app)

@app.route('/')
def home():
    return "<h1>home</h1>"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    pass



if __name__ == "__main__":
    app.debug = True
    app.run()
