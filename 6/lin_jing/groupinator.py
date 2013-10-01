#! /usr/bin/env python

from csv import reader
from random import shuffle

def group(filename):
    f = open(filename, "r")
    classes = {"1": [], "2": []}
    with f:
        for row in reader(f):
            classes[row[0]].append(row[2:])

    count = 4
    for x in classes.values():
        shuffle(x)
        for i in x:
            print "%s,%s,%s" % (count / 4, i[0], i[1])
            count += 1

if __name__ == "__main__":
    group("students")