#hw 4
#Shaan Sheikh
#2013-10-02
import csv
from random import shuffle

per6 = []
per7 = []

with open('students.txt', 'rb') as students:
    reader = csv.reader(students)
    for row in reader:
	if (row[1] == '6'):
		per6.append(row[2:])
	else:
		per7.append(row[2:])

shuffle(per6)
shuffle(per7)

print("Period 6:")
for i in range(len(per6)):
	per6[i].insert(0,str((i+4)/4))
	print(",".join(per6[i]))

print("")
print("Period 7:")
for i in range(len(per7)):
	per7[i].insert(0,str((i+4)/4+8))
	print(",".join(per7[i]))
