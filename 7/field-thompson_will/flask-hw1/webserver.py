from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>Available Files:</h1>"
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # note : though this may seem dangerous, everything in the repo is already available to read
    for f in files:
        html = html + "\n<li><a href="+str(f)+">"+str(f)+"</a></li>"
    html += "\n</ol>"
    return html


@app.route("/<file>")
def clicked(file):
    f = open(file, 'rw')
    s = f.read()
    #f.write("\n"+t)
    f.close()
    return s + '\n<h6><a href="/">HOME</a></h6>'

@app.route("/open/")
@app.route("/open/<arg>")
def open_file(arg='text.txt'):
    f = open(arg, 'rw')
    s = f.read()
    f.close()
    return s + '\n<h6><a href="/">HOME</a></h6>'

if __name__ == "__main__":
    app.debug = True
    app.run()
