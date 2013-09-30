import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():    
    NAMES = ['The Z', 'Brown', 'Weirdo', 'Robert', 'Emily', 'Jabberwocky']

    VERBS = ['fell', 'ran', 'murdered', 'jogged', 'chased', 'stalked']

    PLACES = ['ocean', 'forest', 'lake', 'mountains', 'Jupiter']

    ADJECTIVES = ['evil', 'suicidal', 'homicidal', 'freaky', 'crazy', 'insane']

    NOUNS = ['cheetah', 'cat', 'lion', 'chupacabra', 'centaur', 'minotaur']

    name = random.choice(NAMES)
    verb = random.choice(VERBS)
    place = random.choice(PLACES)
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
          
    return render_template("madlib.html", name = name, verb = verb, place = place, adjective = adjective, noun = noun)


if __name__ == "__main__":
    app.run(debug = True)
