from flask import Flask

from flask import session,url_for,request,redirect,render_template

app = Flask(__name__)
app.secret_key="my secret key"


@app.route("/hidden")
def hidden():
    if 'username' in session:
        return "<h1> in the secret page </h1>"
    else:
        return redirect(url_for('login'))


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
        
@app.route("/reset")
def reset():
    session.pop('count',None)
    return redirect(url_for('home'))


@app.route("/count")
def count():
    try:
        c = session['count']
    except:
        c=0
    c=c+1
    session['count']=c
    page="""
    <h1>The count is: %d</h1>
    <a href="/count">count</a>
    """
    return page%(c)

@app.route("/")
def home():
    #return redirect(url_for('count'))
    return redirect("/count")
    
    


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
    
