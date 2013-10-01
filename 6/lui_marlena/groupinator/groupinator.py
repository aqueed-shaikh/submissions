#!/usr/bin/python
import random

lines = open("students.dat").readlines()

newlines = []
for l in lines:
    newlines.append( l.strip())

pd6 = []
pd7 = []

for x in newlines:
    if x[0] == "1":
        pd6.append(x)
    else:
        pd7.append(x)

<<<<<<< HEAD
for l in pd6:
    print l
=======
for m in pd6:
    m.strip()

random.shuffle(pd6)
counter = 1
group = 1
for m in pd6:
    if counter > 4:
        group = group + 1
        counter = 1
    if group > 8:
        break
    print group
    print m[3:]
    counter = counter + 1


#random.shuffle(pd7)
>>>>>>> 31dfe407e0687162b2bd1e25037a05766b539016
