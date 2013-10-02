#!/usr/bin/python

import random

lines = open("students").readlines()
newlines = []
class1 = []
class2 = []
for I in lines:
    newlines.append(I.strip())

for N in newlines:
    N = N.split(",")
    if N[0] == '1':
        del N[0:2]
        class1.append(N)
    else:
        del N[0:2]
        class2.append(N)

random.shuffle(class1)
random.shuffle(class2)

count = 1
while count <= 8:
    print "%d %s" %(count, list.pop(class1))
    print "%d %s" %(count, list.pop(class1))
    print "%d %s" %(count, list.pop(class1))
    print "%d %s\n" %(count, list.pop(class1))
    count += 1

count = 1
while count <= 8:
    print "%d %s" %(count, list.pop(class2))
    print "%d %s" %(count, list.pop(class2))
    print "%d %s" %(count, list.pop(class2))
    print "%d %s\n" %(count, list.pop(class2))
    count += 1
