from flask import Flask
from flask import render_template

from random import randrange, choice
  
 
app = Flask(__name__)


@app.route("/")
def home():
    pnouns = ["Bob", "Mr. Zamansky", "Helen", "Julie", "Mr. Platek", "Susie", "Mister Rogers", "Salvatore Dali", "Pablo Picasso", "Jimmy Fallon", "Troy", "Abed", "Britta", "Jeff", "Annie", "Shirley", "Pierce", "John", "Hank", "Elmo", "Big Bird", "Mario", "Luigi"]

    nouns = ["rock", "bowl of cereal", "doorknob", "ruler", "toilet paper", "reese's cup", "tissue box", "clock", "lipstick", "eyeliner", "thermometer", "calendar", "candycane", "Christmas tree", "box", "laptop", "flower", "cucumber", "hipster", "meme", "cloud", "penguin"]
    
    #verbs are all in singular past tense and require a direct object
    verbs = ["ate", "found", "killed", "drew", "painted", "gave birth to", "sat on", "saw", "misplaced", "hugged", "grew fond of"]
    
    adjs = ["super ugly", "pretty", "nice", "horrible", "smart", "spectacular", "very unacceptable", "regular, old", "normal", "wonderful", "awesome", "cool", "lame", "sophisticated", "hip", "fashionable", "posh", "sunny", "grimy", "sour"]
    
    places = ["Stuyvesant", "the cafeteria", "the Hudson staircase", "the third floor atrium", "room 307", "the forest", "Hogwarts", "Narnia", "South Korea", "North Korea", "China", "France", "Antarctica", "the library", "the shopping mall", "the subway station", "the dreamatorium", "the study room", "the dark field", "a black hole"]
    
    propnoun= pnouns[randrange(0, len(pnouns))]
    noun= nouns[randrange(0, len(nouns))]
    verb= verbs[randrange(0, len(verbs))]
    adjective= adjs[randrange(0, len(adjs))]
    place= places[randrange(0, len(places))]
    adjective2= adjs[randrange(0, len(adjs))]

    return render_template("mlibs.html", propnoun = propnoun, noun = noun, verb = verb, adjective = adjective, place = place, adjective2 = adjective2)

if __name__=="__main__":
    app.debug=True 
    # 0.0.0.0 means listen on all interfaces
    app.run(host="0.0.0.0",port=5000)
