import random

f = file('res/students.txt')
secs = [[],[]]
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip().split(',')
    secs[int(lines[i][0])-1].append(lines[i][2:])


for sec in secs:
    random.shuffle(sec)

gnum = 0

for sec in secs:
    for i in range(0,len(sec)):
        if i%4 == 0:
            gnum += 1
        print ",".join([str(gnum)] + sec[i])
