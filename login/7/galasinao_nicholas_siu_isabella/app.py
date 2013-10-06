from flask import Flask
from flask import request
from flask import url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is the Home Page</h1>"

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        user={'username':request.form['username'],
              'password':request.form['password']}

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=7777)
