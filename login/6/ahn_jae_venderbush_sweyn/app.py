from flask import Flask

from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve

app = Flask(__name__)
app.secret_key="key"
app.config['SHELVE_FILENAME'] = 'logins.db'
shelve.init_app(app)


@app.route("/hidden")
def hidden():
    if 'username' in session:
        return "<h1> in the secret page </h1>"
    else:
        return redirect(url_for('login'))


@app.route("/login",methods=['GET','POST'])
def login():
    logins = shelve.get_shelve('c')
    if request.method=="GET":
        return render_template('login.html')
    else:
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        if button == "login":
            if username in logins and logins[username]['password'] == password:
                session['username'] = username
                return "Success"
            else:
                return "Username and password not on file"

@app.route("/register", methods=['GET','POST'])
def register():
    logins = shelve.get_shelve('c')
    if request.method=="GET":
        return render_template('register.html')
    else:
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        if button == "Submit":
            if not username in logins:
                logins[username] = {'password':password,'count':8}
                print logins
                return "Successfully created account"
            else:
                return "Username Already Exists"

@app.route("/count")
def count():
    logins = shelve.get_shelve('c')
    try:
        username = session['username']
        print username
    except:
        return "Not logged in"
    try:
        count = logins[username]['count']
    except:
        count = 0
    count += 1
    d = logins[username]
    d['count'] = count
    logins[username] = d
    print logins
    page="""
    <h1>The count is: %d</h1>
    <a href="/count">count</a>
    """
    return page%(count)

@app.route("/")
def home():
    return redirect("/hidden")


if __name__=="__main__":
    app.debug=True
    app.run()
    
