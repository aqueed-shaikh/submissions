#!/usr/bin/env python
import random
from listTools import clearList
from listTools import listLength

lines = open('students').readlines()

lines.sort()

b = True
class6 = []


while (b):
    x = lines.pop(0)
    if ("1" == x[0:1]):
        class6.append(x)
    else:
        lines.insert(0,x)
        b = False

class7 = lines

#print(class6)
#print(class7)

new6 = []
new7 = []

for l in class6:
    new6.append(l.strip())

for l in class7:
    new7.append(l.strip())

#class6 = []
#class7 = []

#for l in new6:
#    class6.append(l.split(","))

#for l in new7:
#    class7.append(l.split(","))

def org(lista, lista2):
    temp = []
    i = 4
    j = 4
    while (j > 0):
        while (i > 0):
            temp.append(lista.pop(random.randint(0, listLength(lista)-1)).split(","))
            i -= 1
#       print(temp)
        lista2.append(temp)
#       print(lista2)
#       clearList(temp)
        temp = []
#       print(temp)
#       print(lista2)
        i = 4
        j -= 1


clearList(class6)
clearList(class7)


org(new6, class6)
org(new7, class7)


def finalize(lista):
    for l in lista:
        for m in l:
            i = 2
            while (i > 0):
                m.pop(0)
                i -= 1
        while (i < 4):
            s = ",".join(l.pop(0))
            l.append(s)
            i += 1

finalize(class6)
finalize(class7)

print("Pd 6 class groups:")
for l in class6:
    print(l)
print("\nPd 7 class groups:")
for l in class7:
    print(l)
    
