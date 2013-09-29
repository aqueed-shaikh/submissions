#########HW done by Hanson Lin and Haoxin Luo ##############
from flask import Flask
from flask import render_template

from random import randrange, choice
  
 
app = Flask(__name__)


@app.route("/")
def home():
    pnouns = ["Hanson","Haoxin","Alvin","Kelvin","Jared","Bradley","Kevin","Kyle","Tim","Tyler","Lizhong","Jason","Michael","Benjamin"]

#    numbers = ["10","20","5","50","2","30","35","45","52","38","13"]

    times = ["6:00", "5:30", "5:00", "6:12", "5:49", "5:45", "6:15", "6:30", "6:45"]

    bodyparts = ["toe", "knee", "arm", "elbow", "wrist", "neck", "crotch", "leg", "foot", "hand", "nose"]

    nouns = ["rock","stick","leaf","bug","twig","sprinkler","squirrel","brick","snail","ball","book","root","pencil"]   

    speakingverbs = ["wailed","cried","screamed","exclaimed","barked","complained","groaned","moaned","screeched","shrieked","whimpered","yelled"]
    
    verbs = ["punched","smacked","kissed","kicked","elbowed","shoved","pushed","nudged","breathed on","looked at"]
    
    adjs = ["ugly","buff","ripped","angry","smelly","lame","tall","giant","wimpy","horrible","grimy","scary"]

    persons = ["biker","gangster","old man","little asian girl","hobo","jogger","thug","student","office man","teenager"]

    adverbs = ["angrily","quickly","suddenly","furiously","clumsily","majestically","suddenly","viciously"]

    person = persons[randrange(0, len(persons))]
    speakingverb = speakingverbs[randrange(0, len(speakingverbs))]
    bodypart = bodyparts[randrange(0, len(bodyparts))]
#    number = numbers[randrange(0, len(numbers))]
    number = randrange(0,60)
    time = times[randrange(0, len(times))]
    propnoun= pnouns[randrange(0, len(pnouns))]
    noun= nouns[randrange(0, len(nouns))]
    verb= verbs[randrange(0, len(verbs))]
    adjective= adjs[randrange(0, len(adjs))]
    adverb = adverbs[randrange(0, len(adverbs))]

    return render_template("madlibs.html", propnoun = propnoun, noun = noun, verb = verb, adjective = adjective, bodypart = bodypart, time = time, number = number, adverb = adverb, speakingverb = speakingverb, person = person)

if __name__== "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5009)
