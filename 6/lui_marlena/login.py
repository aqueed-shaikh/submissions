from flask import Flask
from flask import session, url_for, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'username.db'
shelve.init_app(app)



@app.route("/register", methods = ['GET', 'POST'])
def register():
    #db = shelve.open(   )?
    page="""<h1>Register Here!</h1>
        <form action = "/hidden" method="post">
        username: <input type="text" name="username">
        <br>
        password: <input type="password" name="password">
        <br>
        <input type="submit" name="button" value="register">
        <input type="submit" name="button" value="cancel">
        </form>
        """
   # db = shelve.get_shelve('c')
   # db[request.form['username']] = request.form['password']
    session['username'] = u
    return page

@app.route("/login", methods = ['GET', 'POST'])
def login():
    page="""<h1>Login Here!</h1>
         <form action = "/register" method="post">
         username: <input type "text" name= "username">
         <br>
         password: <input type = "password" name = "password">
         <br>
         <input type= "submit" name = "button" value = "login">
         <input type= "submit" name = "button" value = "cancel">
         <br>
         Not registered yet? No worries, join now!
         <input type = "submit" name = "button" value = "register">
         </form>
         """
    #u = session['username']
    return page

@app.route("/hidden", methods = ['GET', 'POST'])
def hidden():
    page="""
         <form action = "/reset" method = "get">
         <h1>SUCCESS!</h1>
         <br>
         Congratulations, you have logged in successfully.
         <br>
         Ok, that's all we had.
         <br>
         <input type = "submit" name = "button" value = "logout">
         </form>
         """
    return page

@app.route("/reset", methods = ['GET', 'POST'])
def reset():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)
