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
        return redirect("/home")
    else:
        #return redirect(url_for('user'))
        return redirect("/login")


#HOME
@app.route("/home")
def home():
    if 'user' in session:
        page="""
        <h1>Welcome home.</h1>
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
        return render_template("login.html")
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
        return render_template("register.html")
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
        return render_template("register.html")
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
    

 
 


 
   
