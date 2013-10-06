from flask import Flask
from flask import session,url_for,request,redirect,render_template

app = Flask(__name__)

# register
# login
# logout

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register")
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

#@app.route("/login")
#@app.route("/logout")





if __name__ =="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=1337)
