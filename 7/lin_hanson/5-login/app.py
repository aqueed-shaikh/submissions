from flask import Flask
from flask import session, url_for, redirect, render_template, request
import shelve

app = Flask(__name__)
app.secret_key='my secret key'


@app.route("/")
def home():
    if 'username' in session:        
        page = """
        <h1> This is the main page for %s</h1>
        <a href="/logout">Logout</a>
        """
        return page%(session['username'])
                  
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
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html",invalid="False",repeat="False")
    else :
        usernameu = request.form['username']
        username = usernameu.encode('ascii','ignore')
        passwordu = request.form['password']
        password = passwordu.encode('ascii','ignore')
        passwordretypeu = request.form['passwordretype']
        passwordretype = passwordretypeu.encode('ascii','ignore')
        s = shelve.open("sessions")
        if s.has_key(username):
            s.close()
            return render_template("register.html",invalid="False",repeat="True")
        elif password == passwordretype:
            s["%s"%(username)] = password
            s.close()
            session['username'] = username
            return redirect(url_for('home'))
        else:
            s.close()
            return render_template("register.html",invalid="True",repeat="False")


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

    
