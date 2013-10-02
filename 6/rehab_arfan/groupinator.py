# Arfan Rehab, Derek Tang
from random import shuffle

text = open('students').read()
lines = text.split('\n')[:-1]
names = []

for l in lines:
    line = l.split(',')
    period = int(line[1])
    name = ' '.join(line[2:][::-1]

shuffle(names)

groups = []



