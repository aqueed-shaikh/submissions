#!/usr/bin/python

from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask.ext import shelve

app = Flask(__name__)
app.secret_key = 'WOW SUPER SECRET KEY!1!!!!!!!!!!!!!one'
app.config['SHELVE_FILENAME'] = 'data.db'
shelve.init_app(app)
env = app.jinja_env

@app.route('/')
def home():
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username'].encode('ascii', 'ignore')
		password = request.form['password'].encode('ascii', 'ignore')
		db = shelve.get_shelve('c')
		if username in db and db[username] == password:
			session['username'] = username
	
	if session['username'] != none:
		redirect(url_for('page1'))
	return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username'].encode('ascii', 'ignore')
		password = request.form['password'].encode('ascii', 'ignore')
		password_confirm = request.form['password-confirm'].encode('ascii', 'ignore')
		db = shelve.get_shelve('c')
		if password != password_confirm:
			return 'The two passwords are not equal.'
		elif username in db:
			return 'An account already exists with that username'
		else:
			db[username] = password
			return render_template('page2.html')
	return render_template('register.html')

@app.route('/page1')
def page1():
	return render_template('page1.html')

@app.route('/page2')
def page2():
	return render_template('page1.html')

@app.route('/accounts')
def accounts():
	db = shelve.get_shelve('c')
	acc = ""
	for key in db:
		acc += key + ":" + db[key] + "\n"
	return acc

if __name__ == '__main__':
	env.line_statement_prefix = '='
	
	app.debug = True
	app.run(host='0.0.0.0')