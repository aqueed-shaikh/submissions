import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", d = {
            "P1": random.choice(["Brian", "Ben", "Jing"]), 
            "P2": random.choice(["Seven", "Six", "Four", "Roger"]),
            "V1": random.choice(["Kick", "Eat", "Step on", "Laugh at", "Sneeze on", "Chase"]),
            "N1": random.choice(["Trees", "Redbull", "Snicker Bars", "Chikcen Wings", "Mac Keyboards"]),
            "V2": random.choice(["Pray to", "Rub", "Wash", "Touch", "Sing at"]),
            "N2": random.choice(["Cloud", "Mountain", "Chair", "Bacon"]),
            "N3": random.choice(["Cheddar Cheese", "King", "Waffle", "Peanut Butter", "Jelly"]),
            "N4": random.choice(["People", "Flowers", "Grass", "Water", "Mitsubishi"]),
            "N5": random.choice(["Sharnadoes", "Whole Wheat Bread", "Apples", "Frying Pans"]),
            "V3": random.chocie(["Steal", "Devour", "Jumping On", "Crying On", "Licking"]),
            "N6": random.choice(["Lollipops", "Honey", "Bears", "Frogs", "Pigeons"])
        })

if __name__ == "__main__":
    app.run()