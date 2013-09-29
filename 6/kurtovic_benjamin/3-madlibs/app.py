#! /usr/bin/env python
# Team members:
# Ben Kurtovic and Jing Lin

import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("madlibs.html", d = {
            "P1": "Brian", "P2": random.choice(["Seven", "Six", "Four", "Roger"])
        })

if __name__ == "__main__":
    app.run(debug=True)
