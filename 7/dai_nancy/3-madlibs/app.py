from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

words = {"Names": ["Ash", "Gary", "Paul", "May", "Dawn", "Serena", "Brock", "Lance", 
                  "Joey", "Yugi", "Atem", "Bakura", "Ryou", "Tony", "Bob", "Pepper", 
                  "Lucer", "Auffle", "Laim", "Rejek", "Owend", "Wymp", "Wieklin", 
                   "Yami"], 
         "Titles": ["Lass", "Youngster", "Champion", "Bug Boy", "Fisherman", "Hiker", 
                   "Camper", "Rocket Grunt", "Kimono Girl", "Lady", "Pokemon Breeder", 
                   "Rich Boy", "Beauty"],
         "Location": ["Pallet Town", "Lavender Town", "Violet City", "Cerulean", 
                     "New York", "Rome", "Slums of Brookyln", "Jail", 
                      "Little Root Town", "Lilycove City", "Blackthorn City", 
                      "Hogwarts", "Bermuda Triangle"],
         "Pronouns": ["he", "she", "it"],
         "Adjectives": ["happy", "sad", "ugly", "fugly", "disgusting", "greasy", 
                        "sparkling", "fabulous", "flamboyant", "wimpy", "gorgeous", 
                        "pretty", "scrawny", "fat", "obese", "chubby"],
         "Verbs": ["hop", "step", "jump", "sing", "dance", "walk", "fly",
                   "tumble", "trip", "double-layout front summersalt", "mime", 
                   "roll", "hug", "glomp", "drool on"],
         "Pokemon": ["Magikarp", "Bidoof", "Zubat", "Feebas", "Mew", "Arceus", 
                     "Charizard", "Blastoise", "Venasaur", "Pikachu", "Pichu", 
                     "Raichu", "Wailord", "Skitty", "Eevee", "Jolteon", "Espeon",
                     "Mewtwo", "Lucario", "Lugia", "Yugi", "Ho-Oh", "Ditto", 
                     "Ralts", "Pidgey", "Rattata", "Metapod", "Ampharos", "Sunkern",
                     "Diglett", "Rayquaza", "Celebi", "Dragonite"],
         "Level": ["-1000", "0", "5", "10", "50", "100", "3241", 
                   "12", "23", "329", "980", "789", "364", "21", "32"],
         "Nicknames": ["Bum", "Dump", "Derp", "Idjit", "Munion", "Snack", "Chicken", 
                       "Waffle", "Pickle", "Dipshi", "Trainer", "Dipwad", 
                       "Supreme Overlord"],
         "PastVerbs": ["hopped", "stepped", "jumped", "walked", "sang", "danced", 
                       "flew", "tumbled", "tripped", "mimed", "rolled", "hugged", 
                       "glomped", "drooled on"],
         "Adverbs": ["lovingly", "happily", "quietly", "loudly", "slowly",
                     "romantically", "fabulously", "attractively", "festively", "hotly"]
     }

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/madlibs")
def madlibs():
    return render_template(
        "madlibs.html",
        name1 = words["Names"][random.randrange(0, len(words["Names"]))],
        name2 = words["Names"][random.randrange(0, len(words["Names"]))],
        title1 = words["Titles"][random.randrange(0, len(words["Titles"]))],
        title2 = words["Titles"][random.randrange(0, len(words["Titles"]))],
        title3 = words["Titles"][random.randrange(0, len(words["Titles"]))],
        location1 = words["Location"][random.randrange(0, len(words["Location"]))],
        location2 = words["Location"][random.randrange(0, len(words["Location"]))],
        location3 = words["Location"][random.randrange(0, len(words["Location"]))],
        location4 = words["Location"][random.randrange(0, len(words["Location"]))],
        pronoun1 = words["Pronouns"][random.randrange(0, len(words["Pronouns"]))],
        pronoun2 = words["Pronouns"][random.randrange(0, len(words["Pronouns"]))],
        adjective1 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
        adjective2 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
        adjective3 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
        adjective4 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
        adjective5 = words["Adjectives"][random.randrange(0, len(words["Adjectives"]))],
        verb1 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],
        verb2 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],
        verb3 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],
        verb4 = words["Verbs"][random.randrange(0, len(words["Verbs"]))],
        pokemon1 = words["Pokemon"][random.randrange(0, len(words["Pokemon"]))],
        pokemon2 = words["Pokemon"][random.randrange(0, len(words["Pokemon"]))],         
        nickname1 = words["Nicknames"][random.randrange(0, len(words["Nicknames"]))],
        nickname2 = words["Nicknames"][random.randrange(0, len(words["Nicknames"]))],
        level1 = words["Level"][random.randrange(0, len(words["Level"]))],
        level2 = words["Level"][random.randrange(0, len(words["Level"]))],
        adverb1 = words["Adverbs"][random.randrange(0, len(words["Adverbs"]))],
        adverb2 = words["Adverbs"][random.randrange(0, len(words["Adverbs"]))],
        pastverb = words["PastVerbs"][random.randrange(0, len(words["PastVerbs"]))]
    )


if __name__ == "__main__":
    app.debug = True
    app.run()

