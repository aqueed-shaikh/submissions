from flask import Flask
import random as r

app = Flask(__name__)

@app.route('/')
def do_stuff():
    h = r.randrange(0,100)
    return '<h1>random gpa: %i </h1>' % h


if __name__ == '__main__':
    app.run()
