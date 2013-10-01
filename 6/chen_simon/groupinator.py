#Eli Cohen & Simon Chen 

import random


lines = open('students').readlines()
newlines =[]
for l in lines:
    newlines.append(l.strip())
splited = []
for l in newlines:
    splited.append(l.split(','))

period6 = []
period7 = []

for l in splited:
    if l[0] == '1':
        period6.append(l)
    else:
        period7.append(l)
print "Do you want the groups to be random?(yes)"
s = raw_input();
if s == 'yes':
    random.shuffle(period6)
    random.shuffle(period7)

ans = '';

f = 1.0

for l in period6:
    ans += '%d,%s,%s\n' %(f, l[2], l[3])
    f += 0.25

for l in period7:
    ans += '%d,%s,%s\n' %(f, l[2], l[3])
    f += 0.25

print(ans)
