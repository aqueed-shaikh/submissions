from flask import Flask

from flask import session,url_for,request,redirect,render_template

app = Flask(__name__)
app.secret_key="my secret key"

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="GET":
	return render_template("login.html")
    else:
	return render_template("login.html")

@app.route("/")
def home():
    #return redirect(url_for('count'))
    return redirect("/login")

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method=="GET":
	return render_template("register.html")
    else:
	button = request.form['button']
	if button == "Submit":
	    name = request.form['username']
	    password = request.form['password']
	    return redirect("/login")
	else:
	    return render_template("register.html")

@app.route("/success")
def success():
    return "<h1> You have successfully logged in!</h1>"

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
