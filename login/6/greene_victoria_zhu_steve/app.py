#!/usr/bin/python

from flask import Flask, render_template, url_for, redirect, request, session
from flask.ext import shelve
from flask.ext.shelve import get_shelve

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
	error = None
	if request.method == 'POST':
		username = get_form_value('username')
		password = get_form_value('password')
		db = get_shelve('c')
		# add session
		if username in db and db[username] == password:
			session['username'] = username
		else:
			error = 'Incorrect username or password.'
	if logged_in():
		return redirect(url_for('page'))
	return render_template('login.html', title='Login', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		username = get_form_value('username')
		password = get_form_value('password')
		password_confirm = get_form_value('password-confirm')
		db = get_shelve('c')
		if username in db:
			error = 'An account already exists with that username.'
		elif password != password_confirm:
			error = 'The two passwords are not equal.'
		else:
			db[username] = password
			session['username'] = username
			return redirect(url_for('login'))
	if logged_in():
		return redirect(url_for('page'))
	return render_template('register.html', title='Register', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/page')
def page():
	if logged_in():
		return render_template('page1.html', title='Page')
	return redirect(url_for('login'))

@app.route('/accounts')
def accounts():
	db = shelve.get_shelve('c')
	acc = ""
	for key in db:
		acc += key + ":" + db[key] + "<br>"
	return acc

def logged_in():
	return 'username' in session and session['username'] != None

def get_form_value(key):
	return request.form[key].encode('ascii', 'ignore')

if __name__ == '__main__':
	env.line_statement_prefix = '='
	
	app.debug = True
	app.run(host='0.0.0.0')
