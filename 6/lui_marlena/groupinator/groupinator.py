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

for m in pd6:
    m.lstrip("1,6,")

random.shuffle(pd6)
counter = 1
group = 1
for m in pd6:
    if counter > 4:
        group = group + 1
        counter = 1
    print "%d%s" % (group,m[3:])
    counter = counter + 1

random.shuffle(pd7)
counter2 = 1
group2 = 9
for n in pd7:
    if counter2 > 4:
        group2 = group2 + 1
        counter2 = 1
    print "%d%s" % (group2,n[3:])
    counter2 = counter2 + 1
