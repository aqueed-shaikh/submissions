from flask import Flask
from flask import render_template

from random import randrange


app = Flask(__name__)
pnouns = ["Bob", "Mr. Zamansky", "Helen", "Julie", "Mr. Platek", "Susie", "Mister Rogers", "Salvatore Dali", "Pablo Picasso", "Jimmy Fallon", "Troy", "Abed", "Britta", "Jeff", "Annie", "Shirley", "Pierce", "John", "Hank", "Elmo", "Big Bird", "Mario", "Luigi"]

nouns = ["rock", "bowl of cereal", "doorknob", "ruler", "toilet paper", "reese's cup", "tissue box", "clock", "lipstick", "eyeliner", "thermometer", "calendar", "candycane", "Christmas tree", "box", "laptop", "flower", "cucumber", "hipster", "meme", "cloud", "penguin"]

#verbs are all in singular past tense and require a direct object
dverbs = ["ate", "found", "killed", "drew", "painted", "gave birth to", "sat on", "saw", "misplaced"]

adjs = ["super ugly", "pretty", "nice", "horrible", "smart", "spectacular", "very unacceptable", "regular, old", "normal", "wonderful", "awesome", "cool", "lame", "sophisticated", "hip", "fashionable", "posh", "sunny", "grimy", "sour"]

places = ["Stuyvesant", "cafeteria", "Hudson staircase", "third floor atrium", "room 307", "forest", "Hogwarts", "Narnia", "South Korea", "North Korea", "China", "France", "Antarctica", "library", "shopping mall", "subway station", "dreamatorium", "study room", "field"]



@app.route("/")
def home():
    return render_template("mlibs.html", PROPERNOUN = pnoun(), NOUN = noun(), VERB = verb(), ADJECTIVE = adj(), PLACE = place())


def pnoun():
    return pnouns[randrange(0:len(pnouns))]
def noun():
    return nouns[randrange(0:len(nouns))]
def verb():
    return verbs[randrange(0:len(verbs))]
def adj():
    return adjs[randrange(0:len(adjs))]
def place():
    return places[randrange(0:len(places))]

  

if __name__=="__main__":
    app.debug=True 
    # 0.0.0.0 means listen on all interfaces
    app.run(host="0.0.0.0",port=5000)
