from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


@app.route("/kafka")
def kafka():
	troubled = random.choice(['crazy', 'incredible', 'delightful', 'exciting', 'blissful'])
	return render_template("kafka.html",troubled=troubled)

if __name__=="__main__":
	app.run()
