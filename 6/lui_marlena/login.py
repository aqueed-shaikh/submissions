from flask import Flask
from flask import session, url_for, request, redirect, render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'username.db'
shelve.init_app(app)



@app.route("/register")
def register():
    #db = shelve.open(   )?
    page="""<h1>Register</h1>
        <form method="post">
        <input type="text" name="username">
        <input type="text" name="password">
        <input type="submit" name="button" value="register">
        <input type="submit" name="button" value="cancel">
        </form>
        """
   # db = shelve.get_shelve('c')
   # db[request.form['username']] = request.form['password']
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port=5000)
