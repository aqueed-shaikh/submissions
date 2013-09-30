#Team members: Simon Chen & Eli Cohen

from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route("/")
def madLibs():
    n = ['Tim', 'Simon', 'Frankie', 'Siimon' , 'Jonathan Parker', 'Alex', 'Z', 'Tony', 'Sine Nomen', 'Richard', 'Jason', 'Mario', 'Ken', 'Odahviing', 
'God', 'Obama']
    adj = ['bad', 'strong', 'beautiful', 'good', 'fantastic', 'ugly', 'heavy', 'light', 'godli', 'bright', 'weak', 'l33t', 'strang', 'cool']
    place = ['China', 'Forest', 'Road', 'America', 'Orange County', 'Bermuda Triangle', 'Atlantic Ocean', 'Home', 'Nameless City', 'Markarth', 'Riften', 'Solitude', 'nowhere', 'Whole Foods']
    noun = ['noob', 'elite', 'rock', 'cat', 'dog', 'mouse' , 'dragon', 'book', 'SAT', 'Poi', 'pillow', 'sun', 'table', 'bed', 'water', 'fire']
    verb = ['kill', 'destroy', 'help', 'melt', 'smell', 'paint', 'add', 'scam', 'delete', 'integrate', 'grade', 'upload']
    bodypart = ['eye', 'arm', 'leg', 'hair', 'ear', 'face', 'head', 'nose', 'brain', 'small intestine', 'heart', 'digestive system']
    school = ['Stuyvesant High School', 'Bronx Science', 'The Borough of Manhattan Community College', 'Harvard', 'Brooklyn Latin', 'Princeton University', 'Brooklyn Tech', 'Staten Island Tech', 'Hogwarts']  
    random.shuffle(n)
    random.shuffle(adj)
    random.shuffle(place);
    random.shuffle(noun);
    random.shuffle(verb);
    random.shuffle(bodypart);
    random.shuffle(school);
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
         'verb' : verb.pop(),
         'verb1' : verb.pop(),
         'verb2' : verb.pop(),
         'verb3' : verb.pop(),
         'verb4' : verb.pop(),
         'verb5' : verb.pop(),
         'verb6' : verb.pop(),
         'verb7' : verb.pop(),
         'bodypart' : bodypart.pop(),
         'bodypart1' : bodypart.pop(),
         'school' : school.pop(),
         'school1' : school.pop(),
         'noun' : noun.pop(),
         'noun1' : noun.pop(),
         'noun2' : noun.pop(),
         'noun3' : noun.pop(),
         'noun4' : noun.pop(),
         'noun5' : noun.pop(),
         'noun6' : noun.pop(),
         'noun7' : noun.pop(),};
    
    return render_template("madlibs.html", d = d)


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
