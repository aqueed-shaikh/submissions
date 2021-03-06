
# Andrew Zarenberg
# Jae Ahn
# Period 6

from flask import Flask
from flask import render_template
from random import choice

app = Flask(__name__)



fill = {}
fill["place"] = ["New York City",
                 "London",
                 "the middle of the Atlantic Ocean",
                 "hell",
                 "your mom's house",
                 "the center of the Earth"]

fill["animal"] = ["grasshopper",
                  "kangaroo",
                  "baboon",
                  "zebra",
                  "spider",
                  "giraffe",
                  "shark",
                  "legend"]

fill["name"] = ["Master Yi",
                "Tristana",
                "Teemo",
                "Blitzcrank",
                "Donald Trump",
                "Miley Cyrus",
                "Bloomberg",
                "Peter Griffin",
                "your mom",
                "Mr. Zamansky"
                ]





fill["adjective"] = ["funny",
                     "crazy",
                     "perverted",
                     "stupid",
                     "moronic",
                     "gullible",
                     "sexy",
                     "fierce",
                     "sexual",
                     "legendary",
                     "humble"
                     ]

# verb ending in ING
fill["verbING"] = ["eating",
                   "dominating bot lane",
                   "taking down the nexus",
                   "ganking top",
                   "spying on your sister",
                   "studying",
                   "getting drunk",
                   "getting high",
                   "running around naked",
                   "playing the tuba",
                   "coding"
                   ]


# Enter madlibs in the area below using mad.append(" .... ")
# To have it replace words, put in %(TYPE#)s, with TYPE = type of word, and # = word number, starting from 0 and going up
# Each word number is unique... no words will be replaced

# REMEMBER the 's' at the end of %(..)s


mad = []

mad.append( """
Once upon a time in a magical place known as %(place1)s, there lived two legends known as %(name1)s and %(name2)s.  
%(name1)s was a very %(adjective1)s fellow and enjoyed %(verbING1)s on the weekends, whereas
%(name2)s had more %(adjective2)s tastes, and could often be found %(verbING2)s at night.
Differences aside, the two were both quite %(adjective3)s and you could always count on them %(verbING3)s together every day.
However one day when the two were supposed to be %(verbING3)s, %(name1)s didn't show up.  %(name2)s tried calling but to no avail.  
Later that night when %(name2)s was busy %(verbING2)s, %(name1)s called back and explained that they couldn't continue %(verbING3)s together any more.
%(name1)s had moved on and now would only be %(verbING4)s with %(name3)s who was much better in all aspects, especially being much more %(adjective4)s.
%(name2)s was sad and went to the corner to cry, and later died.
""")




madspan = '<span class="mad">%s</span>'


@app.route("/")
def index():
    m = mad[0]


    rep = {}


    for n in fill.keys():
        x = 1

        ta = []
        for p in fill[n]:
            ta.append(p)

        if "("+n+str(x)+")" in m:
            while "("+n+str(x)+")" in m:
                temp = choice(ta)
                rep[n+str(x)] = madspan%(temp)
                ta.remove(temp)

                x += 1


    m = m%(rep)


    return render_template("page.html", madlib=m)




if __name__ == "__main__":
    app.run()



