from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/home")
def home():

	return render_template("madLib.html",d=d)



if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)