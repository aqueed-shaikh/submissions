from flask import Flask
from flask import render_template
import shelve
from random import choice
app = Flask(__name__)

wordsDict = {
            "name":["bob", "joe", "aaron", "sweyn"],
            "noun":["tree", "cow"]
            }


def createDict(d):
    passDict = {}
    for key in d:
        for i in range(d[key]):
            passDict[key+str(i)] = choice(wordsDict[key])
    return passDict

@app.route("/")
@app.route("/<name>")
def root(name="default"):
    values = shelve.open("values/" + name)
    d=createDict(values)
    return render_template(name + ".html", d=d)

@app.route('/favicon.ico')
def favicon():
    pass

if __name__ == "__main__":
    app.run()

