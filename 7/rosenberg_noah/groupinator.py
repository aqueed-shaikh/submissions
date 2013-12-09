#!/usr/bin/python

from random import shuffle

lines = open('students').readlines()

newlines = []


for l in lines:
    newlines.append( l.strip().split(','))

sec1 = []
sec2 = []

for nl in newlines:
    if nl[0] == '1':
        sec1.append(nl)
    elif nl[0] == '2':
        sec2.append(nl)


shuffle(sec1)
shuffle(sec2)

roster = sec1 + sec2
groups = ""
i = 4

for r in roster:
    groups += "%i, %s, %s\n"%(i/4,r[2],r[3])
    i += 1

print groups
