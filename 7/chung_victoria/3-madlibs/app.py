#Team: Glib Dolotov & Victoria Chung

from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
	d={
        "verb": ['troll', 'smack', 'throw',  'talk', 'punch', 'fly', 'jump', 'eat', 'suck', 'bite', 
		 'nudge', 'push', 'struggle', 'hug', 'embrace', 'kiss', 'attack', 'blow', 'smile'],
        "adj" : ['stupid', 'sleepy', 'boring', 'exciting', 'genius', 'great', 'sad', 'happy', 'cocky','interesting', 
		 'wonderful', 'wonderful', 'well', 'ecstatic', 'enthusiastic', 'promising', 'tiring'],
        "adverb" : ['skillfully', 'stupidly', 'quickly', 'slowly', 'quietly', 'elegantly', ],
        "noun": ['hammer', 'white-out', 'textbook', 'sledgehammer', ' marker', 'pipecleaner', 'pig', 'dog', 'cat', 'boyfriend', 'girlfriend',
		 'significant other', 'mother', 'father', 'sister', 'brother', 'priest', 'teacher', 'professor', 'boss', 'coworker'],
        "animal"  : ['pig', 'anteater', 'dog', 'mouse', 'kangaroo', 'koala', 'duck', 'goose', 'deer', 'lion'],
        "body part" : ['leg', 'arm', 'boob', 'foot', 'toe', 'shoulder', 'toe nail', 'nail', 'eyelash','eye' ,'brain',
		       'thumb', 'finger', 'elbow', 'knee', 'ankle', 'nose', 'mouth', 'tongue', 'teeth'],
        "verbed" : ['trolled', 'smacked', 'threw', 'talked', 'punched', 'flew', 'jumped', 'ate', 'sucked','bit',
		    'nudged', 'pushed','struggled', 'hugged', 'embraced', 'kissed', 'attacked', 'blew', 'smiled'],
        "num" : ['1', '0', '9999', '9000', '1000000', '3', '4', '5', '2', '10', '13', '19', '21', '64', '99', '101'],
        "clothing" : ['shirt', 'sweater', 'bra', 'underwear', 'boxers', 'pants', 'shorts', 'tie', 'hoodie', 'hat', 'shoes', 'socks', 'jacket'],
	}
	
	
	return render_template("madlibs.html",
			       n1=d['noun'][random.randrange(0,len(d['noun']))],
			       n2=d['noun'][random.randrange(0,len(d['noun']))],
			       n3=d['noun'][random.randrange(0,len(d['noun']))],
			       adj1=d['adj'][random.randrange(0,len(d['adj']))],
			       adj2=d['adj'][random.randrange(0,len(d['adj']))],
			       adj3=d['adj'][random.randrange(0,len(d['adj']))],
			       adj4=d['adj'][random.randrange(0,len(d['adj']))],
			       num1=d['num'][random.randrange(0,len(d['num']))],
			       num2=d['num'][random.randrange(0,len(d['num']))],
			       verbed1=d['verbed'][random.randrange(0,len(d['verbed']))],
			       animal1=d['animal'][random.randrange(0,len(d['animal']))],
			       verb1=d['verb'][random.randrange(0,len(d['verb']))],
			       verb2=d['verb'][random.randrange(0,len(d['verb']))],
			       bodypart1=d['body part'][random.randrange(0,len(d['body part']))],
			       clothing1=d['clothing'][random.randrange(0,len(d['clothing']))],
			       
			       );
	
