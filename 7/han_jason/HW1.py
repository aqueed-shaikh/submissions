#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World.</h1>\n<h2>More headings</h2>\n<b>Bold stuff</b>"

@app.route("/about")
def about():
    return "<h1>I am cookie monster. Nom nom nom nom.</h1>"

@app.route("/color")
def color():
    return """
<body style='background-color:blue;'>
<h1 style='background-color:white;'>White and blue.</h1>
</body>
"""

@app.route("/table")
def table():
    return """<table border='2'>
<tr>
<td>Yo this is the story</td>
<td>All about how</td>
<td>My life got flip turned</td>
<td>Upside down</td>
</tr>
<tr>
<td>I forget the rest of this song</td>
<td>Oh well</td>
<td>This is a table</td>
<td>wee</td>
</tr>
</table>"""

@app.route("/link")
def link():
    return """<a href="http://www.google.com"></a>"""

@app.route("/list")
def list():
    return """The difference between ul and ol\n
<ul>
<li>This is an unordered list</li>
<li>Stuff</li>
<li>more stuff</li>
<li>even more stuff</li>
<li>aight that's about it</li>
</ul>

<ol>
<li>This list has order.</li>
<li>wee</li>
"""

if __name__ == "__main__":
    app.run()

