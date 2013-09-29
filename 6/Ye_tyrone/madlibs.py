from flask import Flask
from random import randrange

madder = Flask(__name__)

fill = {'names' : ['Peter', 'Mr.Zamanzky', 'Luke',
                  'Piper', 'Louis', 'Kim Jong-il',
                  'Bob', 'Shaggy', 'Jabba'],
        'verbs': ['dance', 'fly', 'shave', 'sleep',
                 'smash', 'kick'],
        'things': ['dogs', 'thongs', 'heads', 'beards',
                  'dragons', 'cards', 'bears']
        }
@madder.route("/")
def go():
    name = fill['names'][randrange(0,9)]
    verb = fill['verbs'][randrange(0,6)]
    thing = fill['things'][randrange(0,7)]
    template= """
%s wanted to %s. So %s %s %s
"""
    return template %(name,verb,name,verb,thing)

if __name__=="__main__":
    madder.debug=True 
    madder.run(host="0.0.0.0",port=5005)
