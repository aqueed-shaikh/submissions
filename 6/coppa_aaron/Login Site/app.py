from flask import Flask
from flask import request, request-handler, session, url_for, render_template
from flask.ext import shelve
users = shelve.get_shelve('users')

app = flask(__name__)
app.route('/')
def home():

app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        #use session dictionary here
        name = request.form['user']
        pswd = request.form['password']
        if(name in users && users[name] == pswd):
            session['username'] = name
            redirect(url_for("page.html"))
        else:
            d = {}
            d['tried'] = 
            return render_template("login.html") #add an error message?

        
app.route("/register", methods=['GET', 'POST'])
def register():
    pass

def page():

    if('username' in session):
        return render_template("page.html", d=session)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
