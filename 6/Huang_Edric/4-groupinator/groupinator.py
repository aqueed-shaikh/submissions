# Groupinator
# Edric Huang & Jane Argodale! 

import random
from random import shuffle

pd6 = []
pd7 = []

lines = open("students.txt").readlines()

for l in lines:
    if l[0] == "1":
        pd6.append(l)
    else:
        pd7.append(l)

for m in pd6:
    m.strip("1,6,")
for n in pd7:
    n.strip("2,7,")

shuffle(pd6)
counter6 = 1
groupnum6 = 1
for m in pd6:
    if counter6 > 4:
        groupnum6 = groupnum6 + 1
        counter6 = 1
    print "%i%s" % (groupnum6,m[3:])
    counter6 = counter6 + 1

shuffle(pd7)
counter7 = 1
groupnum7 = 9
for n in pd7:
    if counter7 > 4:
        groupnum7 = groupnum7 + 1
        counter7 = 1
    print "%i%s" % (groupnum7,n[3:])
    counter7 = counter7 + 1
