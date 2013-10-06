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
        return render_template("login.html")
    else:
        idu = request.form['id']
        id = idu.encode('ascii','ignore')
        s = shelve.open("sessions")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == "GET" :
        return render_template("register.html")

        
@app.route("/members")
def members():
    if 'username' in session:
        page = """
        Hello, this is the member's page.
        """
        return page
    else:
        return redirect("/unknown")

@app.route("/unknown")
def unknown():
    page = """
    <h2> You need to login in</h2>
    <a href="/login">Login here!</a>
    <br>
    <a href="/register">Don't have an account?</a>
    """
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
