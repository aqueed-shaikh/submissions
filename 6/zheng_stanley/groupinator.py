#!/usr/bin/python
import random

lines = open("students.txt").readlines()

#strip the lines
striplines = []
for l in lines:
    striplines.append( l.strip())

#put the students into lists based on periods
period6 = []
period7 = []
for name in striplines:
    if name[0] == "1":
        period6.append(name)
    else:
        period7.append(name)


#prints groups for period 6
#get rid of excess info
#for peers in period6:
#    peers.lstrip("1,6,")
#shuffle period6-(list)
random.shuffle(period6)
counter = 1
group = 1
for peers in period6:
    if counter > 4:
        group = group + 1
        counter = 1
        print ''
    print group, peers[4:]
    counter = counter + 1


#prints groups for period 7
#get rid of excess info
#for others in period7:
#    others.lstrip("2,7,")
#shuffle period7-(list)
random.shuffle(period7)
counter2 = 1
group2 = 9
for others in period7:
    if counter2 > 4:
        group2 = group2 + 1
        counter2 = 1
        print ''
    print group2, others[4:]
    counter2 = counter2 + 1

