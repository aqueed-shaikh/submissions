from flask import Flask

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

@app.route("/index/name")
def name():
    page ="""
        <h2> Cool Stuff will happen. <h2>
"""
    return page

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
