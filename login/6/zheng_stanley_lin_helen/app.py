from flask import Flask
from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'logins.db'
shelve.init_app(app)
app.secret_key="my secret key"



#DEFAULT
@app.route("/")
def home():
    if 'user' in session:
        return render_template('home.html')
    else:
        return redirect("/login")


#LOGIN PAGE    
@app.route("/login",methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        logins = shelve.get_shelve()
        button = request.form['button']
        user = request.form['username']
        passer = request.form['password']
        if button == "Login":
            if not user in logins:
                return redirect("/login")
            elif logins[user] != passer:
                return redirect("/login")
            session['user'] = user
            return redirect("/")
    

#REGISTER
@app.route("/register",methods = ['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html", message = "Type in desired username and password")
    else:
        logins = shelve.get_shelve()
        user = request.form['username'].encode("ascii","ignore")
        passer = request.form['password'].encode("ascii","ignore")
        button = request.form['button']
        if button == "Submit":
            if logins.has_key(user):
                return render_template("register.html", message = "Username is taken")
            else:
                logins[user] = passer
                session['user'] = user
                return redirect("/login")
        elif button == "Back":
            return redirect("/login")


#POP THE USERNAME
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user',None)
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
    

 
 


 
   
