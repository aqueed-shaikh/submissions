from flask import Flask
from flask import request, render_template, redirect, session, url_for
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init(app)
app.secret_key = "my secret key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def home():
    if "username" in sesson:
        return render_template("home.html")
    else:
        return redirect("/login")
      
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    else:
        data = shelve.get_shelve()
        Username = request.form["Username"].encode("ascii", "ignore")
        Password = request.form["Password"].encode("ascii", "ignore")

        if Username in data:
            return "Username exists in the database!"

        elif Password != request.form["Retype"].encode("ascii", "ignore"):
            return "Passwords do not match!"
        
        else:
            users[Username] = Password
            return "Congrats! You have successfully registered!"

@app.route("/login", methods = ['GET', 'POST'])
def login():

@app.route("/logout")
def logout():

    
if __name__ = "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
