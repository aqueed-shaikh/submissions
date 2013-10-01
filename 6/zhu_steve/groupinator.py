#!usr/bin/python
import sys, random

if len(sys.argv) == 1: sys.argv.append("students")

l = [[],[]]
for p in open(sys.argv[1]).readlines():
	p = p.strip().split(',')
	l[int(p[1])-6].append(','.join(p[2:]))

for p in l:
	random.shuffle(p)

l = l[0] + l[1] # people
l = [l[x:x+4] for x in xrange(0, len(l), 4)] # groups
l = [",".join([str(x + 1), group]) for x in xrange(len(l)) for group in l[x]] # people

print '\n'.join(l)