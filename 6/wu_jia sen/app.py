# Jia Sen Wu

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

#funcode, league of legends site rip
@app.route("/league")
def league():
    state = ["Bandle City", "Bilgewater", "Demacia", "Freljord", "Ionia", "Noxus", "Piltover", "Zaun"]
    champion = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Blitzcrank", "Brand", "Caitlyn", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Irelia", "Janna", "Jarvan IV", "Jax", "Jayce", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen", "Kha'Zix", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Pantehon", "Poppy", "Quinn", "Rammus", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xerath", "Xin Zhao", "Yorick", "Zac", "Zec", "Zed", "Ziggs", "Zilean", "Zyra"]
    spell = ["Barrier", "Clairvoyance", "Clarity", "Cleanse", "Exhaust", "Flash", "Ghost", "Heal", "Ignite", "Revive", "Smite", "Teleport", "Fortify", "Promote", "Rally", "Stifle", "Surge"]
    map = ["Crystal Scar", "Howling Abyss", "Magma Chamber", "Proving Grounds", "Summoner's Rift", "Twisted Treeline"]
    
    states = state[random.randrange(0, len(state))]
    champions = champion[random.randrange(0, len(champion))]
    spells = spell[random.rangerange(0, len(spell))]
    maps = map[random.randrange(0, len(map))]
    season = random.randrange(1,2147483648)
    return render_template("league.html", state=states, champion=champions, spell=spells, map=maps, num=season)
    
    
if __name__=="__main__":
    app.debug=True
    # 0.0.0.0 means listen on all interfaces
    app.run(host="0.0.0.0",port=5000)