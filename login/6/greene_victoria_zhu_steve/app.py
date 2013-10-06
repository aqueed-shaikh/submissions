#!/usr/bin/python

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)