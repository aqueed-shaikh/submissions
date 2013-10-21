#!/usr/bin/python
import random

template = "One day %(PROPERNOUN)s was %(VERB)s through the %(PLACE)s. There he found a(n) %(ADJECTIVE)s %(NOUN)s."

i = random.randint(1,10)
pr =["Lilo", "Stitch", "Nemo", "Elmo", "Shrek", "Spongebob", "Bill", "Plankton", "Sandy", "Squishy"]
vb = ["galloping", "paddling", "discouraging", "spinning", "running", "stabbing", "tickling", "shrieking", "folding", "eating"]
pl = ["BMCC", "sushi buffet", "Duane Read", "roof", "cupboard under the stairs", "room 305", "Narnia", "pokeball", "cow", "helicopter", "Starbucks", "Chipotle", "12 GRimmauld Place", "my apartment"]
ad = [ "ugly", "really ugly", "sparkling", "querulous", "facetious", "fulminating" , "phlegmatic", "laconic", "tortuous", "pussilanimous"]
ns = [ "trashcan" , "building", "phone", "cactus", "sun", "folder", "car", "shirt", "fruits", "hair", "lychee"]

d = { 'PROPERNOUN' : random.choice(pr),
      'VERB' : random.choice(vb),
      'PLACE' : random.choice(pl),
      'ADJECTIVE' : random.choice(ad),
      'NOUN' : random.choice(ns)
}


print template %(d)



