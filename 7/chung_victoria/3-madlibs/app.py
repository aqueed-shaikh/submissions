#Team: Glib Dolotov & Victoria Chung

from flask import Flask
from flask import render_template
from random import randrange as rr

app = Flask(__name__)

@app.route("/")
def home():
	s="""
The night was hot and steamy. Luckily, my %(noun)s showed up right on time - he looked like a %(adj)s %(noun)s and smelled like a %(noun)s. Things went %(adj)s for a while, but then it started getting %(adj)s. %(num)s minutes in, he started picking at his %(body part)s and asking if I wanted to %(verb)s it. I, of course, was interested, because that is my favorite activity! Towards the end of the date he %(verbed)s off my %(clothing)s. He was like a wild %(animal)s, Overall, I felt taht the date went %(adverb)s and after at least %(num)s more dates, we might fianlly %(verb)s together in bed!
"""
	d = {
        "verb": ['troll', 'smack', 'throw',  'talk', 'punch', 'fly', 'jump', 'eat', 'suck', 'bite', 'nudge', 'push', 'struggle', 'hug', 'embrace', 'kiss', 'attack', 'blow', 'smile'],
        "adj" : ['stupid', 'sleepy', 'boring', 'exciting', 'genius', 'great', 'sad', 'happy', 'cocky', 'interesting', 'wonderful', 'wonderful', 'well', 'ecstatic', 'enthusiastic', 'promising', 'tiring'],
        "adverb" : ['skillfully', 'stupidly', 'quickly', 'slowly', 'quietly', 'elegantly', ],
        "noun": ['hammer', 'white-out', 'textbook', 'sledgehammer', ' marker', 'pipecleaner', 'pig', 'dog', 'cat', 'boyfriend', 'girlfriend', 'significant other', 'mother', 'father', 'sister', 'brother', 'priest', 'teacher', 'professor', 'boss', 'coworker'],
        "animal"  : ['pig', 'anteater', 'dog', 'mouse', 'kangaroo', 'koala', 'duck', 'goose', 'deer', 'lion'],
        "body part" : ['leg', 'arm', 'boob', 'foot', 'toe', 'shoulder', 'toe nail', 'nail', 'eyelash', 'eye' ,'brain', 'thumb', 'finger', 'elbow', 'knee', 'ankle', 'nose', 'mouth', 'tongue', 'teeth'],
        "verbed" : ['trolled', 'smacked', 'threw', 'talked', 'punched', 'flew', 'jumped', 'ate', 'sucked', 'bit', 'nudged', 'pushed', 'struggled', 'hugged', 'embraced', 'kissed', 'attacked', 'blew', 'smiled'],
        "num" : ['1', '0', '9999', '9000', '1000000', '3', '4', '5', '2', '10', '13', '19', '21', '64', '99', '101'],
        "clothing" : ['shirt', 'sweater', 'bra', 'underwear', 'boxers', 'pants', 'shorts', 'tie', 'hoodie', 'hat', 'shoes', 'socks', 'jacket'],
}
	return s%(d)
	#return s




if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)
