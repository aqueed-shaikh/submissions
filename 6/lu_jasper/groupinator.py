#!/usr/bin/python

import sys
import random 

lines = [p.strip().split(",") for p in open(sys.argv[1]).readlines()]

#for l in newlines: new += l.split(",")
n6 = 1
n7 = 9
k6 = 0
k7 = 0
random.shuffle(lines);

newlines = []

for m in lines:
    if m[1] == '6':
	n = [n6, m[3], m[2]]
	k6 = k6 + 1
	if k6==4:
	    n6 = n6 + 1
	    k6 = 0
    else:
	n = [n7, m[3], m[2]]
	k7 = k7 + 1
	if k7==4:
	    n7 = n7 + 1
	    k7 = 0 
    newlines.append(n)

newlines.sort()

for m in newlines:
    print m

