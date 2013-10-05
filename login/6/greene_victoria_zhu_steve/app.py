#!/usr/bin/python

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return '<html></html>'

@app.route('/login')
def login():
	return render_template('login.html', title='Login', stylesheet=url_for('static', filename='login.css'))

@app.route('/register')
def register():
	return render_template('register.html', title='Register', stylesheet=url_for('static', filename='register.css'))

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)