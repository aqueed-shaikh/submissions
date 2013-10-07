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
    item = ["Abyssal Scepter", "Aegis of the Legion", "Amplifying Tome", "Archangel's Staff", "Athene's Unholy Grail", "Atma's Impaler", "Avarice Blade", "B. F. Sword", "Banner of Command", "Banshee's Veil", "Berserker's Greaves", "Bilgewater Cutlass", "Blackfire Torch", "Blade of the Ruined King", "Blasting Wand", "Bonetooth Necklace", "Boots of Mobility", "Boots of Speed", "Boots of Swiftness", "Brawler's Gloves", "Catalyst the Protector", "Chain Vest", "Chalice of Harmony", "Cloak of Agility", "Cloth Armor", "Crystalline Flask", "Dagger", "Deathfire Grasp", "Doran's Blade", "Doran's Ring", "Doran's Shield", "Eleisa's Miracle", "Elixir of Brilliance", "Exilir of Fortitude", "Emblem of Valor", "Entropy", "Executioner's Calling", "Explorer's Ward", "Faerie Charm", "Fiendish Codex", "Frozen Heart", "Giant's Belt", "Glacial Shroud", "Grez's Spectral Lantern", "Guardian Angel", "Guardian's Horn", "Guinsoo's Rageblade", "Haunting Guise", "Health Potion", "Hexdrinker", "Hextech Gunblade", "Hextech Revolver", "Hextech Sweeper", "Hunter's Machete", "Iceborn Gauntlet", "Ichor of Illumination", "Ichor of Rage", "Infinity Edge", "Ionian Boots of Lucidity", "Kage's Lucky Pick", "Kindlegem", "Kitae's Bloodrazor", "Last Whisper", "Liandry's Torment", "Lich Bane", "Locket of the Iron Solari", "Long Sword", "Madred's Razors", "Mana Manipulator", "Mana Potion", "Manamune", "Maw of Malmortius", "Mejai's Soulstealer", "Mercurial Scimitar", "Mercury's Treads", "Mikael's Crucible", "Moonflair Spellblade", "Morellonomicon", "Muramana", "Nashor's Tooth", "Needlessly Large Rod", "Negatron Cloak", "Ninja Tabi", "Null-Magic Mantle", "Odyn's Veil", "Ohmwrecker", "Oracle's Elixir", "Oracle's Extract", "Orb of Winter", "Overlord's Bloodmail", "Phage", "Phantom Dancer", "Philosopher's Stone", "Pickaxe", "Prospector's Blade", "Prospector's Ring", "Quicksilver Sash", "Rabadon's Deathcap", "Randuin's Omen", "Ravenous Hydra", "Recurve Bow", "Rejuvenation Bead", "Rod of Ages", "Ruby Crystal", "Ruby Sightstone", "Runaan's Hurricane", "Rylai's Crystal Scepter", "Sanguine Blade", "Sapphire Crystal", "Seeker's Armguard", "Seraph's Embrace", "Shard of True Ice", "Sheen", "Shurelya's Reverie", "Sight Ward", "Sightstone", "Sorcerer's Shoes", "Spectre's Cowl", "Spirit of the Ancient Golem", "Spirit of the Elder Lizard", "Spirit of the Spectral Wraith", "Spirit Stone", "Spirit Visage", "Statikk Shiv", "Stinger", "Sunfire Cape", "Sword of the Divine", "Sword of the Occult", "Tear of the Goddess", "The Black Cleaver", "The Bloodthirster", "The Brutalizer", "The Hex Core", "The Lightbringer", "Thornmail", "Tiamat", "Total Biscuit of Rejuvenation", "Trinity Force", "Twin Shadows", "Vampiric Scepter", "Vision Ward", "Void Staff", "Warden's Mail", "Warmog's Armor", "Wicked Hatchet", "Will of the Ancients", "Wit's End", "Wooglet's Witchcap", "Wriggle's Lantern", "Youmuu's Ghostblade", "Zeal", "Zeke's Herald", "Zephyr", "Zhonya's Hourglass"]
	champion = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Blitzcrank", "Brand", "Caitlyn", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Irelia", "Janna", "Jarvan IV", "Jax", "Jayce", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen", "Kha'Zix", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Pantehon", "Poppy", "Quinn", "Rammus", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xerath", "Xin Zhao", "Yorick", "Zac", "Zec", "Zed", "Ziggs", "Zilean", "Zyra"]
    spell = ["Barrier", "Clairvoyance", "Clarity", "Cleanse", "Exhaust", "Flash", "Ghost", "Heal", "Ignite", "Revive", "Smite", "Teleport", "Fortify", "Promote", "Rally", "Stifle", "Surge"]
    map = ["Crystal Scar", "Howling Abyss", "Magma Chamber", "Proving Grounds", "Summoner's Rift", "Twisted Treeline"]
    states = state[random.randrange(0, len(state))]
	items = item[random.randrange(0, len(item))]
    champions = champion[random.randrange(0, len(champion))]
    spells = spell[random.rangerange(0, len(spell))]
    maps = map[random.randrange(0, len(map))]
    season = random.randrange(1,65536)
    return render_template("league.html", state=states, item=items, champion=champions, spell=spells, map=maps, num=season)
    
    
if __name__=="__main__":
    app.debug=True
    # 0.0.0.0 means listen on all interfaces
    app.run(host="0.0.0.0",port=5000)