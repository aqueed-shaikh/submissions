from flask import Flask
from flask import render_template
from flask.ext import shelve

app = Flask(__name__)

@app.route('/')
def home():
	return "<h3> Login </h3>"


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
