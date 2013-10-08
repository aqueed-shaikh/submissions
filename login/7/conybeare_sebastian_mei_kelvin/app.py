from flask import Flask
from flask import session, url_for, redirect, render_template
import login

app = Flask(__name__)
app.secret_key='my secret key'


@app.route("/register")
def register():
	return 'Registration Page'

@app.route("/login")
def login():
	return 'Login Page'

@app.route("/")
def index():
	if 'username' in session:
		return 'congratulations, you have logged in!'
	else:
		return """
		<a href="/login">login</a>\n
		<a href="/register">register</a>
		"""

if __name__ == '__main__':
	app.run()
