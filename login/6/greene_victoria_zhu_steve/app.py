#!/usr/bin/python

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
env = app.jinja_env

@app.route('/')
def home():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

if __name__ == '__main__':
	env.line_statement_prefix = '='
	
	app.debug = True
	app.run(host='0.0.0.0')