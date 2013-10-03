#!/usr/bin/python

from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


d = {
'name':['Tommy', 'Bob', 'Alan', 'Eugene', 'Spongebob', 'Patrick', 'Jon', 'Eric', 'Lucas', 'Richard'],
'place':['park','forest','plantation','school','bank','playground','store','junkyard','factory'],
'verb':['ran','jumped','swam','ate','slept','saw','climbed','cloned','lent','loaned','dunked','fished'],'adjective':['stupid','dumb','retarded','smart','foolish','ridiculous','eager','new','old','young'],
'food':['hamburger','apple','fish','kiwi','orange','sandwich','cereal','cake','pasta','spaghetti','rice','broccoli']}

@app.route("/")
def home():
    return render_template("stuff.html", 
name = random.choice(d['name']),
place1 = random.choice(d['place']), 
place2 = random.choice(d['place']),
place3 = random.choice(d['place']),
verb1 = random.choice(d['verb']), 
verb2 = random.choice(d['verb']), 
verb3 = random.choice(d['verb']), 
adjective1 = random.choice(d['adjective']), 
adjective2 = random.choice(d['adjective']), 
adjective3 = random.choice(d['adjective']), 
food1 = random.choice(d['food']),
food2 = random.choice(d['food']),
food3 = random.choice(d['food']),
food4 = random.choice(d['food']));
#Is there a better way to do this? Without making new variables...

if __name__ == "__main__":
    app.debug = True
    app.run()
