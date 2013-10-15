from flask import Flask
from flask import request, session
from flask import url_for, render_template, redirect
import sqlite3
import auth
import random

app = Flask(__name__)
app.secret_key = 'my secret key'

template="""
<h1>Well here you go</h1>

<p>%(name1)s decided to %(adverb1)s %(verb1)s to the %(place1)s with %(name2)s. They were going there to get a %(thing1)s. After getting said %(thing1)s, the two of them went to the %(place2)s in order to have %(name2)s %(adverb2)s help %(name1)s with %(name1)s's %(thing2)s problem.</p>
<br>
<a href="/madlibs">Randomize!</a>

<br><hr>
<a href="/">HOME</a>
"""


@app.route("/")
def home():
    if 'username' in session:
        page = """
<h1><b><i><u>WELCOME USER</b></i></u></h1>
<br>
<p>OMG what is <a href="/madlibs">this</a>??????</p>
<br><hr>
<p>Would you like to <a href="/logout">Logout?</a></p>

"""
        return page

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
        if auth.authenticate(username,password):
            session['username'] = username
            return redirect('/')
        else:
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
        if auth.add(user, psswd):
            session['username'] = user
            return redirect('/')
        else:
            return render_template("register.html", incorrect="False")
            

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect('/')

@app.route("/madlibs")
def site():
    if 'username' in session:
        verb_list=['jump','walk','slide','skate']
        name_list=['Bob','Jane']
        thing_list=['bat','sandwich','gold bar','poster','clip','shoe']
        adverb_list=['quickly','arduously','sexily','grumpily']
        place_list=["park",'library','store','arcade','basement','pool','sandbox']
    
        d={'name1':name_list.pop(int(random.random()*len(name_list))),
           'verb1':verb_list.pop(int(random.random()*len(verb_list))),
           'thing1':thing_list.pop(int(random.random()*len(thing_list))),
           'adverb1':adverb_list.pop(int(random.random()*len(adverb_list))),
           'place1':place_list.pop(int(random.random()*len(place_list))),
           'name2':name_list.pop(int(random.random()*len(name_list))),
           'thing2':thing_list.pop(int(random.random()*len(thing_list))),
           'adverb2':adverb_list.pop(int(random.random()*len(adverb_list))),
           'place2':place_list.pop(int(random.random()*len(place_list)))
           }
        return template%(d)
            
        


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
