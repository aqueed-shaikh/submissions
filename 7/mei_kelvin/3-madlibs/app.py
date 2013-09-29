from flask import Flask;from flask import render_template;import random

app = Flask (__name__)
template = """
<h1>Cards against Humanity 1</h1>
<p>I'm sorry Professor, but I couldn't complete my homework because of %(answer1)s. </p>
<h1>Cards against Humanity 2</h1>
<p>Instead of coal, Santa now gives the bad children %(answer2)s. </p>
<h1>Cards against Humanity 3</h1>
<p> In Michael Jackson's final moments, he thought about %(answer3)s. </p>
"""

@app.route("/")
def home():
    return " <h1> Home Page </h1> "

@app.route("/madlibs")
def thelists():
    answer1 = ["mom","Stalin","vigilante Justice", "my ex-wife"]
    answer2 = ["Grandpa's ashes", "estrogen", "a 55-gallon drum of lube", "graphic violence, adult language and some sexual content"]
    answer3 = ["dying of dysentery", "peeing a little bit", "coat hanger abortions", "a mating display"]

    stuff = {'answer1':answer1.pop(int(random.random() * 4)), 'answer2' : answer2.pop(int(random.random()*4)), 'answer3': answer3.pop(int(random.random()*4))}
    return template%(stuff)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6969)
    
