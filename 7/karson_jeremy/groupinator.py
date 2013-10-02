#Group Members: Jeremy Karson and Benjamin Attal

#!/usr/bin/python
from random import randrange

lines = open("students").readlines()

#strip and split each element in the "lines" list.
for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(",")

#create a roster for period 6
period6roster = []
for l in lines:
    if l[0] == '1':
        period6roster.append(l)

#create a roster for period 7    
period7roster = []
for l in lines:
    if l[0] == '2':
        period7roster.append(l)

#make a list that will hold each group in period 6
grouplist6 = []
while len(period6roster) != 0:

    #create a 4-person group by selecting 4 random
    #people from the period6roster. Then, remove
    #these people from the roster.
    specificgroup = []
    for i in range (0,4):
        random_index = randrange(0, len(period6roster))
        specificgroup.append(period6roster[random_index])
        period6roster.remove(period6roster[random_index])

    #add the group to the list of groups
    grouplist6.append(specificgroup)

#make a list that will hold each group in period 7
#(see period 6 above).
grouplist7 = []
while len(period7roster) != 0:
    specificgroup = []
    for i in range (0,4):
        random_index = randrange(0, len(period7roster))
        specificgroup.append(period7roster[random_index])
        period7roster.remove(period7roster[random_index])
    grouplist7.append(specificgroup)

#access each group in period 6
for i in range(0, len(grouplist6)):
    #access each person in that group and print their group number,
    #last name, and first name.
    for n in range (0, 4):
        string = str(i+1) + " , " + grouplist6[i][n][2] + " , " + grouplist6[i][n][3]
        print string

#same as above, but now for period 7
for i in range(0, len(grouplist7)):
    for n in range (0, 4):
        string = str(i+9) + " , " + grouplist7[i][n][2] + " , " + grouplist7[i][n][3]
        print string

        

    



