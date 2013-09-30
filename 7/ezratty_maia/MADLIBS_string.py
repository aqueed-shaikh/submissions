#HW3
#Maia and Sabrina
#9/29/13

from flask import Flask

app = Flask(__name__)

@app.route("/<int:num>")
def home(num):
    s = """MASH!!!
    You will live in a %(house)s.
    You will drive a %(color)s %(car)s.
    You will marry %(spouse)s and have %(number)s kids.
    You will be a %(job)s in %(location)s.
    """
    house = ["mansion", "shack", "house", "apartment"]
    color = ["black", "red", "pink", "silver"]
    car = ["porsche", "limo" , "toyota",]
    spouse = ["Jeremy", "Ben", "Justin", "Noah"]
    number = ["2","3","5000","0"]
    job = ["lawyer","plumber","programmer","teacher"]
    location = ["NY","Rome","Paris","NJ"]
    d={'house':house[num],
   'color':color[num],
   'car':car[num],
   'spouse' : spouse[num],
   'number' : number[num],
   'job' : job[num],
   'location' : location[num]}
    return s%(d)

#we didn't use a template because we think this works a little better and it was easier for us to understand

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
    
