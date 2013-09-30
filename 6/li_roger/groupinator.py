#! /usr/bin/env python

import random, math

lines=open("students").readlines()
s = {}
s['6'] = [];
s['7'] = [];
for l in lines:
	l = l.strip().split(",")[1:]
	s[l[0]].append(l[1:])
random.shuffle(s['6'])
random.shuffle(s['7'])
ind = 0
for c in s:
	for l in s[c]:
		ind+=1
		l.insert(0,str(math.ceil(ind/4)))
		print(",".join(l))