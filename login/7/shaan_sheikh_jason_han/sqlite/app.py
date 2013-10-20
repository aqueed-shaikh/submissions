from flask import Flask
from flask import request, render_template, url_for, redirect, session, flash
import cgi
import shelve
import auth

app = Flask(__name__)
app.secret_key ='my secret key'

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('loggedin'))
    else:
        return redirect(url_for('login'))

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
       # if valid_login(request.form["id"],
                      # request.form["pw"]):
        form = cgi.FieldStorage()
        if "Button1" in form:
            ID = request.form['id'].encode('ascii','ignore')
            PW = request.form['pw'].encode('ascii','ignore')
            i = authenticate(ID,PW)
            if i == 0:
        #s = shelve.open("sessions")
            
        #if s.has_key(ID):
        #    if s[ID] == PW:
                session["username"] = ID
                return redirect(url_for('loggedin'))
            elif i == 1:
                flash("Username and Password do not match.")
                return redirect(url_for('login'))
            else:
                flash("Username is not registered in database. Redirecting to Register Page")
                return redirect(url_for('register'))
        #elif "Button2" in form:
        #   return redirect(url_for('register'))
    #else:
       # flash("Invalid Login")
       # return redirect(url_for('login'))
    else:
        return render_template("login.html")


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        ID = request.form['id'].encode('ascii','ignore')
        PW = request.form['pw'].encode('ascii','ignore')
        #s = shelve.open("sessions")
        i = adduser(ID,PW)
        if i == 1:
        #if s.has_key(ID):
        #    s.close()
            return redirect(url_for('register'))
        else:
            s[ID] = PW
            session["username"] = ID
            return redirect(url_for('loggedin'))
    return render_template("register.html")


@app.route("/loggedin", methods = ["GET","POST"])
def loggedin():
    if "username" in session:
        if request.method == "POST":
            return redirect(url_for('logout'))
    return render_template("loggedin.html")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
        
    
if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
