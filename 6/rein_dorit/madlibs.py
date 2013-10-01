#Dorit Rein and Victoria Greene

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    

    template = "Once upon a time, in a far away %s, %s was %s. But he was %s. But the %s %s %s him and banished him. He was forced to flee to %s where he was %s. He screamed out %s and saw %s. He was supposed to go the %s at %s %s with %s, his fiance. But there was nothing he could do because he had been banished. But then, in a sudden turn of %s, he was allowed %s to his home. And they all %s %s ever after."


    Place1 = random.sample(set(["land", "France", "ball", "Berlin", "Punxsutawney", "Madagascar"]),1);
    Place2 = random.sample(set(["land", "France", "ball", "Berlin", "Punxsutawney", "Madagascar"]),1);
    Place3 = random.sample(set(["land", "France", "ball", "Berlin", "Punxsutawney", "Madagascar"]),1);
    Name1 = random.sample(set(["Tommy", "John", "Louis", "Neville", "Estaban", "Leonard"]), 1);
    Name2 = random.sample(set(["Molly", "Emily", "queen", "Louisa", "Tammy", "Lenora"]), 1);
    NewName = random.sample(set(["Vicky", "Emilia", "princess", "Carolina", "Alexa", "Lena"]), 1);
    Gerund = random.sample(set(["playing", "talking", "sleeping", "writing", "pointing", "laughing"]), 1);
    Adjective1 = random.sample(set(["sad", "evil", "angry", "weird", "soft", "bubbly", "squishy"]), 1);
    Adjective2 = random.sample(set(["sad", "evil", "angry", "weird", "soft", "bubbly", "squishy"]), 1);
    Adjective3 = random.sample(set(["sad", "evil", "angry", "weird", "soft", "bubbly", "squishy"]), 1);
    VerbPast1 = random.sample(set(["hated", "died", "lived", "twiddled", "hopped", "communicated"]), 1);
    VerbPast2 = random.sample(set(["hated", "died", "lived", "twiddled", "hopped", "communicated"]), 1);
    Exclamation = random.sample(set(["AHHHH!", "Darn!", "Wow!", "Yum!", "Golly!", "SHOOT!"]), 1);
    Color = random.sample(set(["red", "pink", "blue", "orange", "turquoise", "magenta"]), 1);
    Time = random.sample(set(["midnight", "highnoon", "3 o'clock", "8 o'clock"]), 1);
    VerbInf = random.sample(set(["to dance", "to suit up", "to chat", "to build", "to bake", "to return", "to follow"]), 1);
    VerbInf2 = random.sample(set(["to dance", "to suit up", "to chat", "to build", "to bake", "to return", "to follow"]), 1);
    Noun = random.sample(set(["events", "babies", "books", "water bottles", "hats", "flags"]), 1);
    Adverb = random.sample(set(["happily", "slowly", "annoyingly", "sweetly", "jokingly", "angrily"]), 1);


    result = "A MAD LIBS FAIRYTALE...<br><br>" + template%(Place1, Name1, Gerund, Adjective1, Adjective2, NewName, VerbPast1, Place2, Adjective3, Exclamation, Color, Place3, Time, VerbInf, Name2, Noun, VerbInf2, VerbPast2, Adverb) + "<br><br><a href=/>Fill in new words!</a>";  

    return result


if __name__ == "__main__":
    app.debug = True;
    app.run(host="0.0.0.0", port = 5005)
