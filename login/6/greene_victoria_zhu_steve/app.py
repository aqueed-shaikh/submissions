#!/usr/bin/python

from flask import Flask, render_template, url_for, redirect, request, session
from random import randint
from mongoauth import *

app = Flask(__name__)
app.secret_key = 'WOW SUPER SECRET KEY!!!!!!!!!!!!!!'

def logged_in():
	if not username_exists(session['username']):
		session.pop('username', None)
	return 'username' in session and session['username'] != None

def get_form_value(key):
	return request.form[key].encode('ascii', 'ignore')

@app.route('/')
def home():
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		username = get_form_value('username')
		password = get_form_value('password')
		if validate_user(username, password):
			session['username'] = username
		else:
			error = 'Incorrect username or password.'
	if logged_in():
		return redirect(url_for('page'))
	return render_template('login.html', title='Login', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		username = get_form_value('username')
		password = get_form_value('password')
		password_confirm = get_form_value('password-confirm')
		if username_exists(username):
			error = 'An account already exists with that username.'
		elif password != password_confirm:
			error = 'The two passwords are not equal.'
		else:
			create_user(username, password)
			session['username'] = username
	if logged_in():
		return redirect(url_for('page'))
	return render_template('register.html', title='Register', error=error)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
	if not logged_in():
		return redirect(url_for('login'))

	error = None
	if request.method == 'POST':
		password = get_form_value('password')
		password_confirm = get_form_value('password-confirm')
		if password != password_confirm:
			error = 'The two passwords are not equal.'
		else:
			update_user(username, password)
	return render_template('settings.html', title='Settings', error=error)

@app.route('/page')
def page():
	if not logged_in():
		return redirect(url_for('login'))

	a = randint(0, 2)
	if a == 0:
		title='Hello there!'
		answer='Did you know that the bikini was invented in ancient Rome?'
	else:
		title='Why did the football coach go to the bank?'
		answer='To get his quarterback!!!'
	return render_template('page.html', title=title, answer=answer)

@app.route('/accounts')
def accounts():
	users = get_users_as_list()
	a = ""
	for user in users:
		a += user + "<br>"
	return a

if __name__ == '__main__':
	init_auth(app)
	
	app.jinja_env.line_statement_prefix = '='
	app.debug = True
	app.run(host='0.0.0.0')
