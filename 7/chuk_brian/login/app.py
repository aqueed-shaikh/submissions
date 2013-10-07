from flask import Flask
from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'login.db'
shelve.init_app(app)
app.secret_key="my supersecret key"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=['GET','POST'])
def register():
    page="""<h1>Login</h1>
        <form method="post">
        <input type="text" name="username">
        <input type="text" name="password">
        <input type="submit" name="button" value="login">
        <input type="submit" name="button" value="cancel">
        </form>
        """
    return page

@app.route("/login", methods=['GET','POST'])
def login():
    return "<h1> swag </h1>"

@app.route("/logout")
def logout():
    return "<h1> swag </h1>"
    





if __name__ =="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=1337)
