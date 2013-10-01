#!/usr/bin/python
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

for l in pd6:
    print l
