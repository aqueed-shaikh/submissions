from flask import Flask

here = 0
hoarx = Flask(__name__)

@hoarx.route("/")
def home:
    here = here + 1
    temp = """
<h1>Been here %i times </h1>
<a href = "/out"> Go out? </a>
"""

@hoarx.route("/out")
def out:
    return """
<h1>You're outside the door </h1>
<a href = "/"> Go back? </a>
<a href = "/out/explore">Explore?</a> 
"""

@hoarx.route("/out/explore")
def outExplore:
    return """
<h3>Yousa Sleepy<h3>
<a href = "/"> Go back? </a>
"""
