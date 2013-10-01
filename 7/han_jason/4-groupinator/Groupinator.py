#!/usr/bin/python
from random import shuffle

lines = open("students.txt").readlines()

newlines = []

for l in lines:
    newlines.append(l.strip())

pd6 = []
pd7 = []

for l in newlines:
    if l[0] == "1":
        pd6.append(l)
    else:
        pd7.append(l)

shuffle(pd6)
shuffle(pd7)

#print pd6
#print pd7

ans = ""
inc = 1
num = 1

while pd6:
    if inc > 4:
        inc = 1
        num += 1
    newlines = pd6.pop().split(",")
    ans += str(num) + "," + newlines[2] + "," + newlines[3] + "\n"
    inc += 1
    #Doesn't look very nice but it works...

while pd7:
    if inc > 4:
        inc = 1
        num += 1
    newlines = pd7.pop().split(",")
    ans += str(num) + "," + newlines[2] + "," + newlines[3] + "\n"
    inc += 1

print ans
