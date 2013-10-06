from flask import Flask
from flask.ext import shelve
from flask import session,url_for,request,redirect,render_template


app = Flask(__name__)
app.secret_key="my secret key"
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)

@app.route("/")
def home():
    num = session['count']
    if num == 0
    return redirect("/register")
else 

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method=="GET":
	return render_template("register.html")
    else:
	button = request.form['button']
	if button == "Submit":
	    name = request.form['username']
	    password = request.form['password']
            c = session['count'];
            c=c+1;
            session['count']=c
            db = get_shelve('login_info')
            db ["username"] = name
            app.secret_key=name
            db ["password"] = password
            return redirect("/home")
	else:
	    return render_template("register.html")

@app.route("/success")
def success():
    return "<h1> You have successfully logged in!</h1>"

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
