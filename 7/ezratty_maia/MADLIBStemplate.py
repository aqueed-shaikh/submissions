# HW #3

# Maia Ezratty and Sabrina Khan

# September 29, 2013

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")


def home():
    template = "MASH!!! You will live in a %s. You will drive a %s %s.You will marry %s and have %s kids.You will be a %s in %s."

    house = random.sample(set(["mansion","shack","house","apartement"]), 1);
    color = random.sample(set(["black", "blue", "silver", "red", "pink"]), 1);
    car = random.sample(set(["toyota", "porsche", "ferrari", "pick-up truck", "ice-cream truck"]),1);
    spouse = random.sample(set(["Jeremy","Ben","Justin","Noah","Sweyn"]),1);
    number = random.sample(set(["2", "3", "5000", "10"," 0"]),1);
    job = random.sample(set(["lawyer", "doctor", "plumber", "teacher", "programmer"]),1);
    location = random.sample(set(["New York", "Rome", "Paris", "Istanbul", "Tel Aviv"]),1);
    
    result = template%(house, color, car, spouse, number, job, location);
    return result


if __name__ == "__main__":
    app.debug = True;
    app.run(host="0.0.0.0", port = 5005)

