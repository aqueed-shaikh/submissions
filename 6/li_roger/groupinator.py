#! /usr/bin/env python
import random, math
lines=open("students").readlines()
s = [[],[]]
for l in lines:
	l = l.strip().split(",")[1:]
	s[int(l[0])-6].append(l[1:])
for i in s:
	random.shuffle(i);
for c in range(len(s)):
	for i in range(len(s[c])):
		s[c][i].insert(0,str(math.floor(i/4)+1+c*8))
		print(",".join(s[c][i]))