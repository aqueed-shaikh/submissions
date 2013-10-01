#Group Members: Jeremy Karson and Benjamin Attal

#!/usr/bin/python
from random import randrange

lines = open("classcode/resources/groupinator/students").readlines()

#print lines

#newlines = []
for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(",")

#print lines    

period6roster = []
for l in lines:
    if l[0] == '1':
        period6roster.append(l)
    
period7roster = []
for l in lines:
    if l[0] == '2':
        period7roster.append(l)


grouplist6 = []
while len(period6roster) != 0:
    specificgroup = []
    for i in range (0,4):
        random_index = randrange(0, len(period6roster))
        specificgroup.append(period6roster[random_index])
        period6roster.remove(period6roster[random_index])
    grouplist6.append(specificgroup)

grouplist7 = []
while len(period7roster) != 0:
    specificgroup = []
    for i in range (0,4):
        random_index = randrange(0, len(period7roster))
        specificgroup.append(period7roster[random_index])
        period7roster.remove(period7roster[random_index])
    grouplist7.append(specificgroup)

#access each group in pd6
for i in range(0, len(grouplist6)):
    #access each person
    for n in range (0, 4):
        string = str(i+1) + " , " + grouplist6[i][n][2] + " , " + grouplist6[i][n][3]
        print string

#access each group in pd7
for i in range(0, len(grouplist7)):
    #access each person
    for n in range (0, 4):
        string = str(i+9) + " , " + grouplist7[i][n][2] + " , " + grouplist7[i][n][3]
        print string

        

    



