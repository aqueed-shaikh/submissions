from random import shuffle 

data = "/Users/user/Desktop/submissions/7/Khan_Sabrina/data.txt"
lines  = open(data).readlines()

newlines = []
for l in lines: 
    newlines.append(l.strip())


pdSeven = []
groups = []

for a in range(0,len(newlines)):
    newlines[a] = newlines[a].split(",")

for a in range(len(newlines)/2, len(newlines)):
        pdSeven.append(newlines[a].pop())


shuffle(pdSeven)

j = 0;
i = 9;
while(j <len(pdSeven)):
    template = "Group %d will be %s,%s,%s, and %s\n"
    result = template%(i,pdSeven[j],pdSeven[j+1],pdSeven[j+2],pdSeven[j+3])
    print result
    j = j + 4
    i = i + 1











