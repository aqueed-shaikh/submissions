from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page!!!!!!!"

@app.route("/next")
def next():
    return "This is the next page!"

if __name__ == "__main__":
    app.run()
