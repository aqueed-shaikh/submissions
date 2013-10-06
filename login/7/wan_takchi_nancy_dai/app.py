from flask import Flask
from flask import session, url_for, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'username.db'
shelve.init_app(app)

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="GET":
    page="""
        <h1>Register</h1>
        <form method="post">
        <input type="text" name="username">
        <input type="text" name="password">
        <input type="submit" name="button" value="register">
        <input type="submit" name="button" value="cancel">
        </form>
        """
    username = shelve.get_shelve('c')
    username["username"] = "password"
    return page
    
@app.route("/login",methods=['GET','POST'])
def login():
    if 'user' in session:
        return redirect("/home")
    elif request.method=="GET":
        page="""<h2>Main Page</h2>
        <form method="post">
        Login: <input type="text" name="username" value="username">
        <input type="text" name="password" value="password"> 
        <input type="submit" name="button" value="Login">
        <p>
        Sign up here if you don't have ana ccount. <a href="/register"> Register Now</a>
        </form>
        """
        return page
    else:
        button = request.form['button']
        user = request.form['username']
        passer = request.form['password']
        shelve[user] = passer

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)
