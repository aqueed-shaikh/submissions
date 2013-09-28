from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/madlib")
def generate():
  names = ["John", "Haru", "Dmitry", "Kevin", "Zac"]
  places= ["JFK", "Yoshi Island", "Desertland", "Swampar", "Hell"]
  things= ["toy duckie", "pot", "DS", "cards", "chess piece", "donut", "bat", "time machine", "fortune ball"]
  times = ["five", "one hundred", "one", "a thousand", "eternity"]
  timeunits= ["years", "seconds", "minutes", "hours", "weeks", "millenia"]
  adjs=["fat", "monstrous", "hot", "ugly", "dirty", "beautiful", "cute"]
  drinks=["apple juice", "orange juice", "saliva", "mud", "dirt", "urine", "poop extract"]
  dictionary = {"name" : random.choice(name),
                "place" : random.choice(places),
                "thing" : random.choice(things),
                "time": random.choice(times),
                "timeunit": random.choice(timeunits),
                "adj": random.choice(adjs),
                "drink": random.choice(drinks)
                }
  return render_template("story.html")

if __name__ == '__main__':
  app.debug=True
  app.run()
  
