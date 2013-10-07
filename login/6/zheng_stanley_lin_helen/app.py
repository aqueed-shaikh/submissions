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
        return render_template('home.html',username=session["username"])
    else:
        return redirect("/login")


#LOGIN PAGE    
@app.route("/login",methods=['GET','POST'])
def login():
    logs = shelve.get_shelve()
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['button']
        user = request.form['username']
        passer = request.form['password']
        if button=="Submit":
            if user in logins and logins[user]['password']==passer:
                sessions['username']=username
                return redirect("/")
            else:
                return "INVALID USERNAME AND PASSWORD"
    

#REGISTER
@app.route("/register",methods=['GET','POST'])
def register():
    logins=shelve.get_shelve()
    if request.method=="GET":
        return render_template("register.html")
    else:
        button = request.form['button']
        user = request.form['username']
        passer = request.form['password']
        if button=="Register":
            if not user in logins:
                logins[user] = {'password':passer}
                return "SUCCESS! :D"
            else:
                return redirect("/register")

#POP THE USERNAME
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user',None)
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
    

 
 


 
   
