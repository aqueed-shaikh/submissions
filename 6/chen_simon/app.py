from flask import Flask
from flask import render_template

import random

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


@app.route("/madLibs")
def madLibs():
    n = ['Tim', 'Simon', 'Frankie', 'Siimon' , 'Jonathan Parker', 'Alex', 'Z', 'Tony', 'Sine Nomen', 'Richard', 'Jason', 'Mario', 'Ken', 'Odahviing']
    adj = ['bad', 'strong', 'beautiful', 'good', 'fantastic', 'ugly', 'heavy', 'light', 'godli', 'bright', 'weak', 'l33t', 'strang', 'cool']
    place = ['China', 'Forest', 'Road', 'America', 'Orange County', 'Bermuda Triangle', 'Atlantic Ocean', 'Home', 'Nameless City', 'Markarth', 'Riften', 'Solitude']
    noun = ['noob', 'elite', 'poop', 'diarrhea', 'rock', 'cat', 'dog', 'mouse' , 'dragon', 'book', 'SAT', 'Poi', 'pillow', 'sun', 'table', 'bed', 'water', 'fire']
    random.shuffle(n)
    random.shuffle(adj)
    random.shuffle(place);
    random.shuffle(noun);
    d = {'name' : n.pop(),
         'name1' : n.pop(),
         'name2' : n.pop(),
         'name3' : n.pop(),
         'name4' : n.pop(),
         'name5' : n.pop(),
         'name6' : n.pop(),
         'name7' : n.pop(),
         'adj' : adj.pop(),
         'adj1' : adj.pop(),
         'adj2' : adj.pop(),
         'adj3' : adj.pop(),
         'adj4' : adj.pop(),
         'adj5' : adj.pop(),
         'adj6' : adj.pop(),
         'adj7' : adj.pop(),
         'place' : place.pop(),
         'place1' : place.pop(),
         'place2' : place.pop(),
         'place3' : place.pop(),
         'place4' : place.pop(),
         'place5' : place.pop(),
         'place6' : place.pop(),
         'place7' : place.pop(),
         'noun' : noun.pop(),
         'noun1' : noun.pop(),
         'noun2' : noun.pop(),
         'noun3' : noun.pop(),
         'noun4' : noun.pop(),
         'noun5' : noun.pop(),
         'noun6' : noun.pop(),
         'noun7' : noun.pop(),};
    
    return render_template("madlibs.html", d = d)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
