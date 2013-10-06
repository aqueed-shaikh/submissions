from flask import Flask
#from flask import session,redirect,render_template
from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve



app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'login.db'
shelve.init_app(app)
appt.secret_key="nLOGN"

@app.route("/")
def start():
    if 'username' in session:
        return redirect("/page1")
    else :
        return """
<h1> Welcome <h1>
<a href = "/login">Login</a>
<a href = "/home">Home</a>
"""

@app.route("/login", methods=['GET','POST'])
def login():
    if 'username' in session:
        return redirect("/home")
    else:
        if request.method=="GET":
            return render_template("login.html");
        else:
            usrname = request.form['username']
            pw = request.form['password']
            shelve[usrname] = pw

@app.route("/home")
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        return redirect("/login")

@app.route("/index")
def index():
    if 'username' in session:
        return render_template("index.html")
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect("/")
    
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
