from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

words = {"Names":["Ash", "Gary", "Paul", "May", "Dawn", "Serena", "Brock", "Lance", "Joey", "Yugi", "Atem", "Bakura", "Ryou", "Tony", "Bob", "Pepper", "Lucer", "Auffle", "Laim", "Rejek", "Owend", "Wymp", "Wieklin", "Yami"], 
         "Titles":["Lass", "Youngster", "Champion", "Bug Boy", "Fisherman", "Hiker", "Camper", "Rocket Grunt", "Kimono Girl", "Lady", "Pokemon Breeder", "Rich Boy", "Beauty"],
         "Location":["Pallet Town", "Lavender Town", "Violet City", "Cerulean", "New York", "Rome", "Slums of Brookyln", "Jail", "Little Root Town", "Lilycove City", "Blackthorn City", "Hogwarts", "Bermuda Triangle"],
         "Pronouns":["he", "she", "it"],
         "Adjectives": ["happy", "sad", "ugly", "fugly", "disgusting", "greasy", "sparkling", "fabulous", "flamboyant", "wimpy", "gorgeous", "pretty", "scrawny", "fat", "obese", "chubby"],
         "Verbs":["hop", "step", "jump", "sing", "dance", "walk", "fly", "tumble", "trip", "double-layout front summersalt", "mime", "roll", "hug", "glomp", "drool on"]
         "Pokemon": ["Magic Karp", "Bidoof", "Zubat", "Feebas", "Mew", "Arceus", "Charizard", "Blastoise", "Venasaur", "Pikachu", "Pichu", "Raichu", "Wailord", "Skitty", "Eevee", "Jolteon", "Espeon", "Mewtwo", "Lucario", "Lugia", "Yugi", "Ho-Oh", "Ditto", "Ralts", "Pidgey", "Rattata", "Metapod", "Ampharos", "Sunkern", "Diglett", "Rayquaza", "Celebi", "Dragonite"],
         "Level":["-1000", "0", "5", "10", "50", "100", "3241", "12", "23", "329", "980","789", "364", "21", "32"],
         "Nicknames":["bum", "dump", "derp", "idjit", "munion", "snack", "chicken", "waffle", "pickle", "dipshi", "trainer", "dipwad", "Supreme Overlord"],
         "Verbed": ["hopped", "stepped", "jumped", "walked", "sang", "danced", "flew", "tumbled", "tripped", "mimed", "rolled", "hugged", "glomped", "drooled on"],
         "Adverbs": ["lovingly", "happily", "quietly", "loudly", "slowly", "romantically", "fabulously", "attractively", "festively", "hotly"]
}

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/madlibs")
def madlibs():
    return render_template("madlibs.html",
                           name1 = words["Names"][random.randrange(0, len(words["Names"]))],
                           name2 = words["Names"][random.randrange(0, len(words["Names"]))],
                           title = words["Titles"][random.randrange(0, len(words["Titles"]))],
                           location = words["Location"][random.randrange(0, len(words["Location"]))],
                           pronoun1 = words["Pronouns"][random.randrange(0, len(words["Pronouns"]))],
                           pronoun2 = words["Pronouns"][random.randrange(0, len(words["Pronouns"]))],
                           adjective1 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
                           adjective2 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
                           adjective3 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
                           verb1 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],
                           verb2 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],
                           verb3 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],


                           pokemon1 = words["Pokemon"][random.randrange(0, len(words["Pokemon"]))],
                           pokemon2 = words["Pokemon"][random.randrange(0, len(words["Pokemon"]))],                          
                           nickname = words["Nicknames"][random.randrange(0, len(words["Nicknames"]))],
                           level = words["Level"][random.randrange(0, len(words["Level"]))],
                           adverb = words["Adverbs"][random.randrange(0, len(words["Adverbs"]))],
                           pastverb = words["Verbed"][random.randrange(0, len(words["Verbed"]))]
                           

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port = 5000))

