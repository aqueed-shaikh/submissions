import random

lines = open("students.txt").readlines()
for i in range (len(lines)):
    lines[i] = lines[i].split(",")

for i in range (len(lines)):
    lines[i][3] = lines[i][3][:-1]

P6 = []
P7 = []

def isNotEmpty(list):
    if len(list) != 0:
        return True
    else: 
        return False


for i in range (len(lines)):
    if lines[i][0] == '1':
        P6.append(lines[i])
    if lines[i][0] == '2':
        P7.append(lines[i])

numba = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8]
a = 0
c = 0
Groups = []

while isNotEmpty(P6):
    b = int(random.random() * (len(P6) - 1))
    Groups.append([numba[a], P6[b][2], P6.pop(b)[3]])
    a = a + 1

while isNotEmpty(P7):
    b = int(random.random() * (len(P7) - 1))
    Groups.append([numba[c], P7[b][2], P7.pop(b)[3]])
    c = c + 1


newfile = open ("Groups.txt", "w")
for i in range(len(Groups)):
    newfile.write (str(Groups[i][0]) + "," + Groups[i][1] + "," + Groups[i][2] + "\n")

newfile.close()
    
