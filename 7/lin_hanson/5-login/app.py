from flask import Flask
from flask import session, url_for, redirect, render_template, request
import shelve

app = Flask(__name__)
app.secret_key='my secret key'


@app.route("/")
def home():
    if 'username' in session:        
        return "<h1> This is the main page for %s</h1>"%(username)
    else:
        return redirect(url_for('login'))

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html",invalid="False")
    else:
        usernameu = request.form['username']
        username = usernameu.encode('ascii','ignore')
        passwordu = request.form['password']
        password = passwordu.encode('ascii','ignore')
        s = shelve.open("sessions")

        if s.has_key(username) and s["%s"%(username)] == password:
            session['username'] = username
            s.close()
            return redirect(url_for('home'))
        else:
            s.close()
            return render_template("login.html",invalid="True")


@app.route("/logout")
def reset():
    session.pop('count',None)
    #return redirect("/count")
    return redirect(url_for('login'))

@app.route("/register")
def register():
    return render_template("register.html")
#@app.route('/count')
#def count():
#    if 'count' in session:
#        c = session['count']
#    else:
#        c=0
#    c=c+1
#    session['count']=c
#    page="""
#    <h1>The count is %d</h1>
#    <a href="/count">Add One</a>
#    <a href="/reset">Reset</a>
#    """
#    return page%(c)

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

    
