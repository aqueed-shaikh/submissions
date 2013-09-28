import random

from flask import Flask
from flask import render_template

app = Flask(__name__)

WORDS = {
    'propernoun': ('Steve', 'Jasper', 'Roger', 'Ben', 'Jing', 'Jason', 'Marlena', 'Jane', 'Pascu'),
    'noun': ('laptop', 'clock', 'chair', 'gun', 'clock', 'toilet'),
    'verb': ('runs', 'shoots', 'kills', 'steals', 'saves', 'naps'),
    'adjective': ('fabulous', 'harmonious', 'wordy', 'slow', 'fast', 'dumb'),
    'place': ('McDonalds', 'Sydney', 'Burger King', 'the Sahara', 'Google Headquarters')
}

l = [WORDS[key][random.randrange(len(WORDS[key]))] for key in WORDS]

print l


@app.route("/")
def madlibs():
    return render_template('madlibs.html', l=l)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5005)