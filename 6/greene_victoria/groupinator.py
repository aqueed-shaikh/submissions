#GROUPINATOR!!!
#By Victoria Greene and Dorit Rein

from flask import Flask
import random

app = Flask(__name__)

pd6 = []
pd7 = []

lines = open("students").readlines()
for line in lines:
    if (line[0] == '1'):
        pd6.append(line[4:])
    else:
        pd7.append(line[4:])
        
def shuffleandcombine(c1,c2):
    random.shuffle(c1)
    random.shuffle(c2)
    combined = c2 + c1
    return combined

@app.route("/")
def home():
    class1 = shuffleandcombine(pd6,pd7);
    groups = "SOFTDEV GROUPS:<br><br>"
    i = 0
    while len(class1) > 0:
        groups += (str)(i/4+1) + "," + class1.pop() + "<br>"
        i += 1
    groups += "<br><a href=/>Make new groups</a>"
    return groups

if __name__ == "__main__":
    app.debug = True
    app.run()
