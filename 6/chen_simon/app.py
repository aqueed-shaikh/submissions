from flask import Flask
from flask import render_template

import random

app = Flask(__name__)


@app.route("/index")
def index():
    page = """
          <h1>This is my first page</h1>
          <ul>
          <li> 1 This is cool</li>
          <li> 2 Hello, World</li>
          <li> 3 First attempt</li>
          <li> 4 </li>
          </ul>
          """
    return page


@app.route("/madLibs")
def madLibs():
    n = ['Tim', 'Simon', 'CoolMan']
    random.shuffle(n)
    d = {'name' : n.pop()}
    return render_template("madlibs.html", d = d)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
