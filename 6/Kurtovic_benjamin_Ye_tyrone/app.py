from flask import Flask
from flask import session,redirect,render_template
#from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve



app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'login.db'
shelve.init_app(app)
appt.secret_key="nLOGN"

@app.route("/")
def home():
    return """
<h1> Welcome <h1>
<a href = "/login">Login</a>
<a href = "/home">Home</a>
"""

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("login.html");
    else:
        
    
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
