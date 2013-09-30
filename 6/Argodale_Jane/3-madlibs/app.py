from flask import Flask
from flask import render_template
import random

app = Flask(__name__)


@app.route("/kafka")
def kafka():
	troubled = random.choice(['crazy', 'incredible', 'delightful', 'exciting', 'blissful'])
	horrible = random.choice(['cute', 'fluffy', 'fat', 'super kawaii'])
	vermin = random.choice(['cat','guinea pig', 'bunny', 'hamster', 'poodle'])
	armour = random.choice(['rug','wool','satin','cushion'])
	brown = random.choice(['big','furry','fuzzy','pudgy'])
	domed = random.choice(['swollen','bouncy','rotund','matted'])
	divided = random.choice(['divided','separated','split'])
	arches = random.choice(['spots', 'stripes', 'splotches','polka dots'])
	stiff = random.choice(['colorful','soft','elegant','pretty'])
	many = random.choice(['little', 'four', 'fuzzy wuzzy'])
	pitifully = random.choice(['adorably', 'elegantly', 'comfortably'])
	thin = random.choice(['long', 'short', 'sleek', 'fat', 'downy'])
	helplessly = random.choice(['energetically', 'excitedly', 'enthusiastically','quickly'])
	return render_template("kafka.html",troubled=troubled, horrible=horrible,vermin=vermin,armour=armour,brown=brown,domed=domed,divided=divided,arches=arches,stiff=stiff,many=many,pitifully=pitifully,thin=thin,helplessly=helplessly)

if __name__=="__main__":
	app.run()
