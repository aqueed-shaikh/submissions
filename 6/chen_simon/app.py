from flask import Flask
from flask import render_template

#Made by Simon Chen and Eli Cohen

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

@app.route("/")
def home():
    page = """
           <h1> MadLibs</h1>
           <h2> What is MadLibs?</h1>
           Mad Libs is a phrasal template word game where one player prompts another for a list of words to substitute for blanks in a story, before reading the - often comical or nonsensical - story aloud. The game is frequently played as a party game or as a pastime.
           <br>
           -Wiki
           <br>
           <br>
           <br>
           First story is at /madlibs
           <br>
           Second story is at /madlibs2

           """
    return page


@app.route("/madlibs")
def madLibs():
    n = ['Tim', 'Simon', 'Frankie', 'Siimon' , 'Jonathan Parker', 'Alex', 'Z', 'Tony', 'Sine Nomen', 'Richard', 'Jason', 'Mario', 'Ken', 'Odahviing','Eli']
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
         'noun7' : noun.pop()};
    
    return render_template("madlibs.html", d = d)

@app.route("/madlibs2")
def madlibs2():
    n = ['Tim', 'Simon', 'Frankie', 'Siimon' , 'Jonathan Parker', 'Alex', 'Z', 'Tony', 'Sine Nomen', 'Richard', 'Jason', 'Mario', 'Ken', 'Odahviing','Eli']
    noun = ['noob', 'elite', 'poop', 'diarrhea', 'rock', 'cat', 'dog', 'mouse' , 'dragon', 'book', 'SAT', 'Poi', 'pillow', 'sun', 'table', 'bed', 'water', 'fire']
    place = ['China', 'Forest', 'Road', 'America', 'Orange County', 'Bermuda Triangle', 'Atlantic Ocean', 'Home', 'Nameless City', 'Markarth', 'Riften', 'Solitude']
    adj = ['bad', 'strong', 'beautiful', 'good', 'fantastic', 'ugly', 'heavy', 'light', 'godli', 'bright', 'weak', 'l33t', 'strang', 'cool']
    verb = ['kill', 'destroy', 'help', 'melt', 'smell', 'paint', 'add', 'scam', 'delete', 'integrate', 'grade', 'upload']
    bodypart = ['eye', 'arm', 'leg', 'hair', 'ear', 'face', 'head', 'nose', 'brain', 'small intestine', 'heart', 'digestive system']
    school = ['Stuyvesant High School', 'Bronx Science', 'The Borough of Manhattan Community College', 'Harvard', 'Brooklyn Latin', 'Princeton University', 'Brooklyn Tech', 'Staten Island Tech', 'Hogwarts']  
    random.shuffle(n)
    random.shuffle(noun)
    random.shuffle(verb)
    random.shuffle(bodypart)
    random.shuffle(school)
    random.shuffle(place)
    random.shuffle(adj)
    d= {'name' : n.pop(),
        'name1' : n.pop(),
        'name2' : n.pop(),
        'name3' : n.pop(),
        'school' : school.pop(),
        'place1' : place.pop(),
        'bodypart' : bodypart.pop(),
        'bodypart1' : bodypart.pop(),
        'bodypart2' : bodypart.pop(),
        'noun' : noun.pop(),
        'noun1' : noun.pop(),
        'noun2' : noun.pop(),
        'noun3' : noun.pop(),
        'noun4' : noun.pop(),
        'noun5' : noun.pop(),
        'verb' : verb.pop(),
        'verb1' : verb.pop(),
        'verb2' : verb.pop(),
        'verb3' : verb.pop(),
        'noun1' : noun.pop(),
        'place2' : place.pop(),
        'place3' : place.pop(),
        'place4' : place.pop(),
        'place' : place.pop(),
        'adj' : adj.pop(),
        'adj1' : adj.pop(),
        'adj2' : adj.pop(),
        'adj3' : adj.pop(),
        }
    return render_template("madlibs2.html", d = d)
    

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
