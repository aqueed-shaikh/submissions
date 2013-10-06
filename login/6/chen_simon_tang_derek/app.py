from flask import Flask
from flask import session, url_for, request, redirect, render_template
import shelve

app = Flask(__name__)
app.secret_key = "my secret key"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET" :
        page = """<h1>Login</h1>
        <br>
        <h3> Please login to continue </h3>
        <form method = "post">
        <h4>Username:</h4>
        <input type ="text" name = "username">
        <br>
        <h4>Password:</h4>
        <input type ="text" name = "password">
        <br>
        <input type ="submit" name = "button" value = "login">
        <input type ="submit" name = "button" value = "cancel">
        """
        return page
    
    

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
