#!/usr/bin/python

#Isabella Siu & Judy Mai

from random import shuffle

lines = open("students.txt").readlines()

newlines = []
for l in lines:
    newlines.append(l.strip().split(','))

pd6 = []
pd7 = []

for l in newlines:
    if l[0] == "1":
        pd6.append(l[2:])
    else:
        pd7.append(l[2:])

shuffle(pd6)
shuffle(pd7)

group = 1
count = 0

for student in pd6:
    if count == 4:
        group += 1
        print str(group) + "," + ",".join(student)
        count = 1
    else:
        print str(group) + "," + ",".join(student)
        count += 1

group = 9
count = 0
for student in pd7:
    if count == 4:
        group += 1
        print str(group) + "," + ",".join(student)
        count = 1
    else:
        print str(group) + "," + ",".join(student)
        count += 1 

