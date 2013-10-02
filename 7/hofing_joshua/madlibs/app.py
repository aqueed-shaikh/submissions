from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Johnny', 'Suzy', 'Manny', 'Cynthia']
    verbs = ['jumped', 'sat', 'played', 'killed']
    places = ['woods', 'park', 'lake']
    adjectives = ['blue', 'red', 'homicidal', 'joyous']
    nouns = ['stick', 'dog', 'life presever']
    d = { 'name': random.choice(names),
            'verb': random.choice(verbs),
            'place': random.choice(places),
            'adjective': random.choice(adjectives),
            'noun': random.choice(nouns)
        }
    return render_template('header.html') + render_template('madlib.html',d=d) + render_template('footer.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
