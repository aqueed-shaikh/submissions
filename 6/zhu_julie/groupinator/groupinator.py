
from random import shuffle

lines = open("students").readlines()
newlines = []
for l in lines: newlines.append(l.strip())
    
P6 = []
P7 = []

for element in newlines:
    if element[0] == "1":
        P6.append(element)
    else:
        P7.append(element)

shuffle(P6)
shuffle(P7)


group = 1
current = 1
for i in P6:
    s = "".join(i)
    print ("%d,%s")%(group, s[4:])
    current = 1 + current 
    if current > 4:
        group = 1 + group
        current = 1
for j in P7:
    s = "".join(j)
    print ("%d,%s")%(group, s[4:])
    current = 1 + current
    if current > 4:
        group = 1 + group
        current = 1
