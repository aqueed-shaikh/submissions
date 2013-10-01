#! /usr/bin/env python
import random, math
s = [[],[]]
[s[int(l.split(",")[0])-1].append(l.strip().split(",")[2:]) for l in open("students").readlines()]
[random.shuffle(i) for i in s]
[print(str(math.floor(i/4)+1)+","+(",".join((s[0]+s[1])[i]))) for i in range(len(s[0]+s[1]))]