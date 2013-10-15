from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
import sqlite3


app = Flask(__name__)
app.secret_key = "cookies"
app.config["SHELVE_FILENAME"] = 'shelves.db'

@app.route("/")
def home():
    return render_template ("index.html")
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template ("login.html")
    else:
        usern = request.form['Username']
        passw = request.form['Password']
        connection = sqlite3.connect('stuff.db')
        connection.execute ("CREATE table if not exists JUMP(usern TEXT, passw TEXT)")
        stuff = connection.execute('SELECT passw from JUMP where usern="%s"' %usern)
        morestuff = [line for line in stuff]
        if len(morestuff) > 0 and morestuff[0][0] == passw:
            session['Username'] = usern
            return redirect ("/success")
        else: 
            return redirect ("/login")


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template ("register.html")
    else:
        connection = sqlite3.connect("stuff.db")
        usern = request.form["Username"]
        passw = request.form["Password required"]
        cpassw = request.form["Confirm Password"]
        connection.execute ("CREATE table if not exists JUMP(usern TEXT, passw TEXT)")
        stuff = connection.execute('SELECT usern from JUMP where usern = "%s"'%usern)
        morestuff = [line for line in stuff]
        if len(morestuff) != 0:
            return redirect ("/error")
        elif passw != cpassw:
            return redirect ("/login")
        else:
            connection.execute('INSERT into JUMP values ("%s","%s")' %(usern,passw))
            connection.commit()
            connection.close()
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
