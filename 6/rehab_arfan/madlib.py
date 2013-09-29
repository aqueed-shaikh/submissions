from random import randrange
from flask import Flask, render_template

app = Flask(__name__)

NAMES = ['Crazy', 'Insane', 'The Z', 'Brown', 'Weirdo']

VERBS = ['fell', 'ran', 'murdered', 'jogged', 'chased']

PLACES = ['ocean', 'grass', 'forest', 'lake']

ADJECTIVES = ['evil', 'suicidal', 'homicidal', 'freaky']

NOUNS = ['meow', 'roar', 'cheetah', 'cat']

@app.route("/")
def home():
    d = { 'name' : NAMES[randrange(len(NAMES))],
          'verb' : VERBS[randrange(len(VERBS))],
          'place' : PLACES[randrange(len(PLACES))],
          'adjective' : ADJECTIVES[randrange(len(ADJECTIVES))],
          'noun' : NOUNS[randrange(len(NOUNS))]
        }
    
    return render_template('index.html', d = d)


if __name__ == "__main__":
    app.run()
