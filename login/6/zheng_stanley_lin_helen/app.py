from flask import Flask
from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve


app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'login.db'
shelve.init_app(app)
app.secret_key="my secret key"



#DEFAULT
@app.route("/")
def home():
    if 'user' in session:
        return render_template("page")
    else:
        #return redirect(url_for('user'))
        return redirect("/login")


#HOME
@app.route("/home")
def home():
    if 'user' in session:
        page="""
        <h1>HOME</h1>
        <p>
        <a href="/logout">Logout</a href>
        """
        return page
    else:
        return redirect("/login")


#LOGIN PAGE    
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
        Don't have an account? <a href="/register"> Register Now</a>
        </form>
        """
        return page
    else:
        button = request.form['button']
        user = request.form['username']
        passer = request.form['password']
        shelve[user] = passer
#            if button=="Login" and user=="username":
 #               return redirect(url_for('redo'))
  #          else:
   #             return redirect(url_for('user'))
            
            
#LOGIN FAILURE----> TRY AGAIN
@app.route("/redo",methods=['GET','POST'])
def redo():
    if request.method=="GET":
        page="""<h1>Main Page</h1>
        <form method="post">
        Invalid Username: Try again
        <p>
        Login: <input type="text" name="username" value="username">
        <input type="text" name="password" value="password">
        <input type="submit" name="button" value="Login">
        <p>
        
        Don't have a Username? <a href="register"> Register Now</a>
        </form>
        """
        return page
    else:
        button = request.form['button']
        user = request.form['username']
        if button=="Login" and user=="username":
            return redirect(url_for('redo'))
        else:
            return redirect(url_for('user'))
    


#REGISTER
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="GET":
        page="""
        <h1>Register</h1>
        <form method="post">
        <input type="text" name="username" value="username">
        <input type="text" name="password" value="password">
        <p>
        <input type="submit" name="button" value="Register">
        <input type="submit" name="button" value="Cancel">
        </form>
        """
        return page
    else:
        button = request.form['button']
        if button=="Register":
            session['username']="username"
            return page

#POP THE USERNAME
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user',None)
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
    

 
 


 
   
