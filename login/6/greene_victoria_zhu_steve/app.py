#!/usr/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return '<html></html>'

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)