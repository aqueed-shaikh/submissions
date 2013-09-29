from flask import Flask;from flask import render_template;import random

app = Flask (__name__)

@app.route("/")
def home():
    return " <h1> Home Page </h1> "

@app.route("/madlibs")
def thelists():
    answer1 = ["mom","Stalin","vigilante Justice", "my ex-wife"]
    answer2 = ["Grandpa's ashes", "estrogen", "a 55-gallon drum of lube", "graphic violence, adult language and some sexual content"]
    answer3 = ["dying of dysentery", "peeing a little bit", "coat hanger abortions", "a mating display"]

    return render_template("template.html", answer1 = random.choice(answer1), answer2 = random.choice(answer2), answer3 = random.choice(answer3))

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=6969)
    
