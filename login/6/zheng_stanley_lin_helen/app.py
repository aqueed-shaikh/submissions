from flask import Flask
from flask import request, render_template, redirect, url_for, session
import sqlite3
import auths

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'logins.db'
app.secret_key="my secret key"



#DEFAULT
@app.route("/home")
def home():
    if 'user' in session:
        return render_template('home.html')
    else:
        return redirect("/login")



#LOGIN PAGE    
@app.route("/login",methods = ['GET','POST'])
def login():
    user_info = sqlite3.connect('SQL_usernames')
    userSQL = user_info.cursor()
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if auths.check(user_info, username, password):
            session["username"] = username
            return redirect(url_for("login"))
        else:
            return redirect(url_for("home"))
    


#REGISTER
@app.route("/register",methods = ['GET','POST'])
def register():
    users_info = sqlite3.connect('SQL_usernames')
    users_info.execute('''
    CREATE TABLE if not exists auths (username TEXT, password TEXT)
    ''')
    if request.method == "GET":
        return render_template("register.html", message = "Type in desired username and password")
    else:
       username = request.form["username"]
       password = request.form["password"]
       if auths.usernameExists(users_info, username):
           return render_template("register.html")
       else:
           auths.add(users_info, username, password)
           return redirect(url_for("home"))



#POP THE USERNAME
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user',None)
    return redirect("/home")


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
