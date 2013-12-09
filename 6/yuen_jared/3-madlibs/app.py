# Jia Sen Wu && Jared Yuen

from flask import Flask
from flask import render_template
from flask import request

import random


app = Flask(__name__)


@app.route("/")
def lottery():
    ball1 = random.randrange(1,57)
    ball2 = random.randrange(1,57)
    ball3 = random.randrange(1,57)
    ball4 = random.randrange(1,57)
    ball5 = random.randrange(1,57)
    megaball = random.randrange(1,47)
    return render_template("index.html",name=request.remote_addr,num1=ball1,num2=ball2,num3=ball3,num4=ball4,num5=ball5,num6=megaball)

@app.route("/madlibs")
def madlibs():
    pnoun = [ "Dursley", "Claus", "Brown", "Zamansky", "Platek", "Jaishankar", "Wu", "Yuen"]
	adj = ["normal", "crazy", "stupid", "annoying", "caring", "benevolent", "lazy", "awkward", "awful"]
	pnouns = pnoun[random.randrange(0, len(pnoun))]
	adjs = adj[random.randrange(0, len(adj))]
	return render_template("madlibs.html", propernoun=pnouns, adjective=adjs)

	
if __name__=="__main__":
    app.debug=True
    # 0.0.0.0 means listen on all interfaces
    app.run(host="0.0.0.0",port=5000)