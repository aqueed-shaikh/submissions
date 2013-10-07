from flask import Flask
from flask import request
from flask import url_for, render_template, redirect, session
import shelve

app = Flask(__name__)
app.secret_key = 'my secret key'



@app.route("/")
def home():
    if 'username' in session:
        return "<h1> The main page</h1>"
    else:
        return redirect(url_for('login'))

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html", incorrect="False")
    else:
        a = request.form['username']
        username = a.encode('ascii','ignore')
        b = request.form['password']
        password = b.encode('ascii','ignore')
        s = shelve.open("sessions")
        if s.has_key(username) and s["%s"%(username)] == password:
            session['username'] = username
            s.close()
            return redirect('/')
        else:
            s.close()
            return render_template("login.html", incorrect="True")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method =="GET":
        return render_template("register.html")
    else:
        temp=request.form['username']
        user=temp.encode('ascii','ignore')
        temp2=request.form['password']
        psswd=temp2.encode('ascii','ignore')
        s = shelve.open("sessions")
        s["%s"%(user)]=psswd
        s.close()
        return redirect("/")
            
        


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
