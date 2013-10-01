#!/usr/bin/python

import random

lines = open("students").readlines()

pd6 = [l.strip()[4:] for l in lines if l[0] == '1']
pd7 = [l.strip()[4:] for l in lines if l[0] == '2']

def group(list, gnum):
    ret = []
    random.shuffle(list)
    i = 0
    for item in list:
        print str(gnum) + "," + item
        i += 1
        if (i % 4 == 0):
            gnum += 1

group(pd6, 1)
group(pd7, 9)
