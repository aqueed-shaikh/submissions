from flask import Flask
from flask import render_template
from random import randrange as rnum
app = Flask(__name__)

@app.route("/")
def home ():
    return "welcome home"

@app.route ("/matlib")

def madlib():

    pool={
        "adj" : ["fat", "ugly", 'smart', 'mad' 'ready', 'happy', 'crazy'],
        "verb": ['run', 'jump', 'swim', 'help', 'scream', 'blow', 'type'],
        "name": ['David', 'Hank', 'he', 'she', 'Sophie', ],
        "noun": ['table', 'chair', 'golf ball' , 'computer', 'painting'],
        "body_part": ['hand', 'lips', 'nose', 'eyes', 'arm'],
        "number" : ['10', '20', '30']
    }

    return render_template("madlib.html", 
                           adj1 = pool["adj"][rnum (0, len(pool["adj"]))],
                           verb1 = pool["verb"][rnum (0, len(pool ["verb"]))],
                           body_part1 = pool["body_part"][rnum (0, len(pool["body_part"]))],
                           number1 = pool["number"][rnum (0, len (pool["number"]))],
                           noun1 = pool['noun'][rnum (0, len (pool['noun']))],
                           verb2 = pool["verb"][rnum (0, len(pool["verb"]))],
                           verb3 = pool["verb"][rnum (0, len(pool["verb"]))],
                           name = pool['name'][rnum (0, len (pool["name"]))],
                           name2 = pool["name"][rnum (0, len (pool["name"]))],
                           name3 = pool["name"][rnum (0, len (pool["name"]))]
                           
                       )
    

if __name__=="__main__":
    app.debug=True 
    # 0.0.0.0 means listen on all interfaces
    app.run(host="0.0.0.0",port=5005)

    
