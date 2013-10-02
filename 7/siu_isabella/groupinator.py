#!/usr/bin/python
#Isabella Siu and Judy Mai
from random import shuffle


lines = open("students").readlines()

newlines = []
for l in lines:
    newlines.append(l.strip().split(','))

pd5 = []
pd6 = []

for l in newlines:
    if l[0] == "1":
        pd5.append(l[2:])
    else:
        pd6.append(l[2:])

shuffle(pd5)
shuffle(pd6)
group = 1
count = 0

for student in pd5:
    if count == 4:
        group += 1
        print str(group) + "," + ",".join(student)
        count = 1
    else:
        print str(group) + "," + ",".join(student)
        count += 1

group = 9
count = 0
for student in pd6:
    if count == 4:
        group += 1
        print str(group) + "," + ",".join(student)
        count = 1
    else:
        print str(group) + "," + ",".join(student)
        count += 1
