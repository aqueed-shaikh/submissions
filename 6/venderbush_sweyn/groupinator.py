import csv
import random

file = open("/Users/sweyn/Dropbox/School/SoftDev/classcode/resources/groupinator/students")
read = csv.reader(file)

students1 = []
students2 = []

for row in read:
    if row[0] == "1":
        students1.append(row)
    else:
        students2.append(row)

random.shuffle(students1)
random.shuffle(students2)

groups1 = []
groups2 = []
groupnum = 1

for student in range(0,len(students1),4):
    group = []
    group.append([groupnum, students1[student][2], students1[student][3]])
    group.append([groupnum, students1[student+1][2], students1[student+1][3]])
    group.append([groupnum, students1[student+2][2], students1[student+2][3]])
    group.append([groupnum, students1[student+3][2], students1[student+3][3]])
    groups1.append(group)
    groupnum += 1

for student in range(0,len(students2),4):
    group = []
    group.append([groupnum, students2[student][2], students2[student][3]])
    group.append([groupnum, students2[student+1][2], students2[student+1][3]])
    group.append([groupnum, students2[student+2][2], students2[student+2][3]])
    group.append([groupnum, students2[student+3][2], students2[student+3][3]])
    groups2.append(group)
    groupnum += 1


for group in groups1:
    for member in group:
        print "%s,%s,%s" % (str(member[0]), member[1], member[2])
for group in groups2:
    for member in group:
        print "%s,%s,%s" % (str(member[0]), member[1], member[2])





