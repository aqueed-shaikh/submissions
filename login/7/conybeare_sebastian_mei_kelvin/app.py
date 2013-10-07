from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
from flask.ext import shelve

app = Flask(__name__)
app.secret_key = "cookies"
app.config["SHELVE_FILENAME"] = 'shelves.db'
shelve.init_app(app)

@app.route("/")
def home():
    return render_template ("index.html")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    lists = shelve.get_shelve('c')
    if request.method == "GET":
        return render_template ("login.html")
    else:
        button = request.form['button']
        if button  == 'Enter':
            usern = request.form['Username']
            passw = request.form['Password']
            if usern in lists and lists[usern] == passw:
                session['Username'] = username
                return redirect ("/success")
            else: 
                return redirect ("/login")


@app.route("/register", methods = ["GET","POST"])
def register():
    lists = shelve.get_shelve('c')
    if request.method == "GET":
        return render_template ("register.html")
    else:
        if request.method == "POST":
            usern = request.form["Username"]
            passw = request.form["Password"]
            cpassw = request.form["Confirm Password"]
            if usern in lists:
                return redirect ("/error")
            elif passw != cpassw:
                return redirect ("/error")
            else:
                lists[usern] = {passw}
                return redirect ("/login")
@app.route("/success")
def sucess():
     return render_template ("LoginSuccess.html")

@app.route("/error")
def error():
    return render_template ("Error.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6969)
