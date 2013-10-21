from flask import Flask
from flask import session,url_for,request,redirect,render_template
import random
from pymongo import MongoClient

client = MongoClient()
db = client['users']
collection = db['info']

app = Flask(__name__)
app.secret_key="my supersecret key"

#breakline~~~~~~~~~~homecode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/")
def home():# this page doesn't do anything it just redirects to the login page
    return redirect("/login")

#breakline~~~~~~~~~~logincode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/login", methods=['GET','POST'])
def login():
    #coding how the login page will look
    page ="""<h1>It's the Login Page FOOL!</h1>
        <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" name="button" value="login">
        <input type="submit" name="button" value="reset"><br><br><br><br><br><br><br>
        I pity the fool that don't have an account!<br>
        <input type ="submit" name="button" value="sign up"><br><br><br>
        Want to change your password?
        <input type = "submit" name = "button" value = "change password">
        <br><br><br><br><br><br><br><br>
        <h6>Website by Mr T</h6>
        </form>"""
    #if someone goes to this website, the page will be shown
    if request.method == "GET":
        return page
    #if someone sends a POST message, that means info is sent in those text boxes. That data is recorded here
    else:
        button = request.form['button']
        if button=="login":
            submitpage = "<h1>submitted fool!</h1>"
            username = request.form['username']
            password = request.form['password']
            if (collection.find_one({'username':username, 'password':password}) == None):
                return redirect(url_for('login'))
            else:
                session["username"] = username
                return redirect('/madlib')
        elif button=="reset":
            return redirect ("/login")
        elif button == "change password":
            return redirect ("/changepass")
        else:
            return redirect ("/register")

#breakline~~~~~~~~~~logoutcode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/logout")
def logout(): #This page just pops you from the session
    session.pop('username', None)
    return redirect("/login")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/changepass", methods = ['GET', 'POST'])
def changepass():
    page = """
<h1>Change password screen</h1><br><br>
<form method = "post">
Username: <input type = "text" name = "username"><br>
Old password: <input type = "password" name = "oldpass"><br>
New Password: <input type = "password" name = "newpass"><br>
<input type = "submit" name = "button" value = "submit changes"><br>
<input type = "submit" name = "button" value = "do not make changes">
</form>"""
    if request.method == "GET":
        return page
    else:
        button = request.form['button']
        if button=="submit changes":
            username = request.form['username']
            oldpass = request.form['oldpass']
            newpass = request.form['newpass']
            if (collection.find_one({'username':username, 'password':oldpass}) == None):
                return redirect("/changepass")
            else:

                #line that doesn't work!!!
                return collection.update({'username':username}, {'$set':{'password':newpass}})

        else:
            return redirect("/login")

#breakline~~~~~~~~~~registercode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
@app.route("/register", methods=['GET','POST'])
def register():
    page="""<h1>Signup page's here fool!</h1>
        <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" name="button" value="sign up">
        <input type="submit" name="button" value="reset"><br><br><br><br><br><br>
        Fool already got a account? Get back in the game!<br>
        <input type ="submit" name="button" value="sign in">
        </form>
        """
    if request.method == "GET":
        return page
    else:
        button = request.form['button']
        if button=="sign up":
            submitpage = "<h1>signed up fool!</h1>"
            username = request.form['username']
            password = request.form['password']
            _user=username.encode('ascii','ignore')
            _pass=password.encode('ascii','ignore')
            user = {'username':_user, 'password':_pass}
            collection.insert(user)
            return redirect ("/login")
        elif button=="reset":
            return redirect ("/register")
        else:
            return redirect ("/login")

#breakline~~~~~~~~~~otherpage1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/madlib", methods = ['GET', 'POST'])
def madlib():
    if 'username' in session:
        template="""
                 <h1>Add some madlibs foo</h1>

                 <p>%(name1)s decided to %(adverb1)s %(verb1)s to the %(place1)s with %(name2)s. They were going there to get a %(thing1)s. After getting said %(thing1)s, the two of them went to the %(place2)s in order to have %(name2)s %(adverb2)s help %(name1)s with %(name1)s's %(thing2)s problem.</p>
<form method="post">
<br><br><br> 
<input type = "submit" name = "button" value = "logout"><br><br><br>
<input type = "submit" name = "button" value = "other page"><br>
</form>
"""        
        
        verb_list=['jump','walk','slide','skate']
        name_list=['Bob','Jane']
        thing_list=['bat','sandwich','gold bar','poster','clip','shoe']
        adverb_list=['quickly','arduously','sexily']
        place_list=["park",'library','store','arcade','basement','pool','sandbox']

        
        d={'name1':name_list.pop(int(random.random()*len(name_list))),
           'verb1':verb_list.pop(int(random.random()*len(verb_list))),
           'thing1':thing_list.pop(int(random.random()*len(thing_list))),
           'adverb1':adverb_list.pop(int(random.random()*len(adverb_list))),
           'place1':place_list.pop(int(random.random()*len(place_list))),
           'name2':name_list.pop(int(random.random()*len(name_list))),
           'thing2':thing_list.pop(int(random.random()*len(thing_list))),
           'adverb2':adverb_list.pop(int(random.random()*len(adverb_list))),
           'place2':place_list.pop(int(random.random()*len(place_list)))
           }
        page = template%(d)
        if request.method == "GET":
            return page
        else:
            button = request.form['button']
            if button=="logout":
                return redirect('/logout')
            else:
                return redirect('/otherpage')
    else:
        return redirect(url_for('/login'))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

@app.route("/otherpage")
def otherpage():
    if 'username' in session:
        return "<h1> Would you like to hear a joke? Yes? Great!</h1><br> A man walked into a bar... ouch!"
    else:
        return redirect("/login")

if __name__ =="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=1337)
