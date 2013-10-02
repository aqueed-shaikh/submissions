#!flask/bin/python

from flask import Flask
from flask import render_template
from random import randrange as rnum

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/demo")
def demo():
    d={'name':"Clyde Thluffy Sinclair",
       'age':"4",
       'rootsfor':['NY Giants','Michigan Wolverines',
                   'Anyone playing the Eagles or Cowboys',
                   'Not the NY Skankees']}
    
    page = render_template("demo.html",d=d)
    return page

@app.route("/luckyt")
@app.route("/luckyt/<n>")
def luckyt(n=None):
    luckynum = random.randrange(0,100)
    return render_template("lucky.html",
                           name=n,
                           num=luckynum)

@app.route("/luckynumber")
@app.route("/luckynumber/<name>")
def number(name="Moe"):
    page=template1%(name,random.randrange(0,100))
    return page
    

@app.route("/who")
@app.route("/who/<name>")
def name(name="default"):
    page = """
    <h1> the page name </h1>
    This is a page with someone's name
    <hr>
    The name is: 
    """
    page=page+name+"<hr>"
    return page

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"

@app.route("/madlib")
def madlib(): 

    pool = {
        "adj" : ["beautiful", "cool", "snazzy"] , 
        "verb" : ["eat", "sleep", "code"] , 
        "name" : ["Mr. Z", "Mr. DW", "Brown-Mykolyk"]
    }

    return render_template("rock.html",
                        adj = pool["adj"][rnum (0, len (pool["adj"]))],
                        verb = pool["verb"][rnum (0, len (pool["verb"]))],
                        name = pool["name"][rnum (0, len (pool["name"]))],
                       )


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
