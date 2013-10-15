from flask import Flask
from flask import request
from flask import render_template
from flask import request, session
from flask import redirect, url_for
import shelve

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
        usern = request.form['Username'].encode('ascii','ignore')
        passw = request.form['Password'].encode('ascii','ignore')
        log = shelve.open("sessions")
        if (log.has_key(usern) and log[usern]==passw):
            log.close()
            session['Username'] = usern
            return redirect ("/success")
        else: 
            log.close()
            return redirect ("/login")


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template ("register.html")
    else:
        log = shelve.open("sessions")
        usern = request.form["Username"].encode('ascii','ignore')
        passw = request.form["Password required"].encode('ascii','ignore')
        cpassw = request.form["Confirm Password"].encode('ascii','ignore')
        if usern in log:
            log.close()
            return redirect ("/error")
        elif passw != cpassw:
            log.close()
            return redirect ("/login")
        else:
            log[usern] = passw
            log.close()
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
