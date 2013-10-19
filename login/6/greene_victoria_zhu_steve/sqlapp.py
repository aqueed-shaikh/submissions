#!/usr/bin/python

from flask import Flask, render_template, url_for, redirect, request, session
import sqlite3, random

app = Flask(__name__)
app.secret_key = 'WOW SUPER SECRET KEY!!!!!!!!!!!!!!'
env = app.jinja_env

con = sqlite3.connect('sqldata.db')
with con:
	con.cursor().execute('CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)')

def print_tables():
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
	print cur.fetchall()

def get_users():
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT * FROM Users')
	return cur.fetchall()

def create_user(username, password):
	con = sqlite3.connect('sqldata.db')
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO Users(username, password) VALUES("%s", "%s")' % (username, password))

def username_exists(username):
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT password FROM Users WHERE username = "%s" LIMIT 1' % username)
	return cur.fetchone() != None

def validate_user(username, password):
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT password FROM Users WHERE username = "%s" LIMIT 1' % username)
	p = cur.fetchone()
	return p != None and p[0] == password

def logged_in():
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
    return redirect('/')

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

@app.route('/page')
def page():
	if logged_in():
		a = random.randint(0, 2)
		if a == 0:
			return render_template('page1.html', title='Hello there!')
		else:
			return render_template('page2.html', title='Want to hear a joke?')
	return redirect(url_for('login'))

@app.route('/accounts')
def accounts():
	users = get_users()
	a = ""
	for user in users:
		a += '|'.join(str(i) for i in user) + "<br>"
	return a

if __name__ == '__main__':
	env.line_statement_prefix = '='
	app.debug = True
	app.run(host='0.0.0.0')