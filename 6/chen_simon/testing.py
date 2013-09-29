from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/home")
def home():
    page = """
          <h1>MadLibs</h1>
          <ul>
          <li> 1 This is cool</li>
          <li> 2 Hello, World</li>
          <li> 3 First attempt</li>
          <li> 4 </li>
          </ul>
          """
    return page

@app.route("/index/name")
def name():
    page ="""
        <h2> Cool Stuff will happen. <h2>
"""
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
