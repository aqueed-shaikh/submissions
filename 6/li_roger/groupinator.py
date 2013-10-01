#! /usr/bin/env python
import random, math
s = [[],[]]
for l in open("students").readlines():
	l = l.strip().split(",")[1:]
	s[int(l[0])-6].append(l[1:])
[random.shuffle(i) for i in s]
s = s[0] + s[1]
[print(str(math.floor(i/4)+1)+","+(",".join(s[i]))) for i in range(len(s))]