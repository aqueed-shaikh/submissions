from flask import Flask

from flask import session,url_for,request,redirect,render_template

import auth

app = Flask(__name__)
app.secret_key="key"

@app.route("/hidden")
def hidden():
    if 'username' in session:
        return "<h1> This is a hidden page to confirm you are logged in as %s</h1>" % session['username']
    else:
        return redirect(url_for('login'))


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        if button == "Submit":
            if auth.checkLogin(username,password):
                session['username'] = username
                return """
                Success
                <a href="/"><span class="s1">Return to Homepage</span></a>
                """
            else:
                return "Username and password not on file"

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method=="GET":
        return render_template('register.html')
    else:
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        if button == "Submit":
            if not auth.checkUsername(username):
                auth.addLogin(username, password)
                return "Successfully created account"
            else:
                return """
                Username Already Exists
                <p>
                <a href="/register"><span class="s1">Try Again</span></a>
                """

@app.route("/count")
def count():
    try:
        username = session['username']
    except:
        return "Not logged in"
    auth.incrementCount(username)
    count = auth.getCount(username)
    page="""
    <h1>The count is: %d</h1>
    <p>  
    <a href="/count">
    <input type="button" name="button" value="Increment Count">
    </a> 
    </p>
    """
    return page%(count)

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('logout.html')
    else:
        return redirect('/')

@app.route("/")
def home():
    try:
        username = session['username']
        return render_template('Home.html',username=username)
    except:
        return redirect(url_for('login'))

if __name__=="__main__":
    auth.setup()
    app.debug=True
    app.run()
    
