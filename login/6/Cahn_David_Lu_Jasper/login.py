from flask import Flask

from flask import session,url_for,request,redirect,render_template

app = Flask(__name__)
app.secret_key="my secret key"

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="GET":
        page="""<h1>Login</h1>
        <form method="post">
        <input type="text" name="username">
        <input type="text" name="password">
        <input type="submit" name="button" value="login">
        <input type="submit" name="button" value="cancel">
        </form>
        """
        return page
    else:
        
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
	else


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
