#!usr/bin/python

import sys
import random

from flask import Flask

people = [p.strip().split(',') for p in open(sys.argv[1]).readlines()]

periods = [[], []]
for person in people:
	index = int(person[0]) - 1
	periods[index].append(','.join([person[2], person[3]]))

for period in periods:
	random.shuffle(period)


people = periods[0] + periods[1]
groups = [people[x:x+4] for x in xrange(0, len(people), 4)]
people = [",".join([str(x + 1), b]) for x in xrange(len(groups)) for b in groups[x]]

print people


app = Flask(__name__)