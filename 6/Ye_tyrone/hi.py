from flask import Flask

here = 0
hoarx = Flask(__name__)

@hoarx.route("/")
def home:
    here = here + 1
    temp = """
<h1>Been here %i times </h1>
<a href = "/out"> go out? </a>
"""

@hoarx.route("/out")
def out:
    return """
<h1>You're out </h1>
<a href = "/"> go back? </a>
"""
