from flask import Flask
from flask import session, request, render_template, url_for, redirect
import cgi
import shelve

app=Flask(__name__)

loggedin = False

@app.route("/")
def home():
    if loggedin == True:
        return "<h1>This is the home page</h1>"
    else:
        return redirect(url_for('login'))

app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = cgi.FieldStorage()
        if "Login" in form:
            idu = request.form['id']
            id = idu.encode('ascii','ignore')
            s.shelve.open("sessions")
            
            if s.has_key(id):
                s.close()
                global loggedin
                loggedin = True
                return redirect(url_for('session'))
            else:
                s.close()
                return redirect(url_for('register'))
                
        else:
            return redirect(url_for('register'))

app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        idu = request.form['id']
        id = idu.encode('ascii','ignore')
        s.shelve.open("sessions")
        
        if s.has_key(id):
            s.close()
            return redirect(url_for('register')) #too lazy to post an "id already taken" message
        else:
            s[id] = 0
        s.close()
        return redirect(url_for('login'))

app.route("/session",methods = ["GET","POST"])
def session():
    if loggedin:
        if request.method == "GET":
            return render_template("session.html")
        else:
            form = cgi.FieldStorage()
            if "Logout" in form:
                global loggedin
                loggedin = False
                return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
        


if __name__ =="__main__":
    app.debug = True
    app.run(host = "0.0.0.0",port = 5000)
