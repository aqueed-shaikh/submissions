from flask import Flask, render_template, request
app = Flask(__name__)
d={
    'name': 'Jade',
    'gender': 'Female',
    'possessive': 'her',
    'pronoun': 'her',
    'subject': 'she',
    'color': 'green',
    'food': 'cake',
    'bff': 'Dave',
    'critter1': 'dragon',
    'critter2': 'sky-whale',
    'sound': 'roar'}

def resetDictionary():
    d={
        'name': 'Jade',
	'gender': 'Female',
	'possessive': 'her',
	'pronoun': 'her',
	'subject': 'she',
	'color': 'green',
	'food': 'cake',
	'bff': 'Dave',
	'critter1': 'dragon',
	'critter2': 'sky-whale',
	'sound': 'roar'}
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/", methods=['POST'])
def story():
    resetDictionary()
    #d['name']= request.form['name'].capitalize()
    #d['color']= request.form['color'].lower()    
    if request.form['gender'] == 'Male': 
        d['gender']='Male'
        d['possessive']= 'his'
        d['pronoun']= 'him'
        d['subject']= 'he'
    for key,data in request.form.items():
        if data != "" :
            d[key] = data.lower()
    d['name'] = d['name'].capitalize()
    return render_template("story.html", d=d)
   
@app.route("/story-default/")
def storydefault():
    return render_template("story.html",d=d)

if __name__=='__main__':
    app.debug=True
    app.run()
