from random import shuffle 

#This part creates a list lines where each line of the data is an element
data = "/Users/Maia/data.txt"
lines  = open(data).readlines()

#This gets rid of the newline thing
newlines = []
for l in lines: 
    newlines.append(l.strip())
#This  puts everyone from period 7's name into the array.
pdSeven = []

for a in range(0,len(newlines)):
    newlines[a] = newlines[a].split(",")

for a in range(len(newlines)/2, len(newlines)):
        pdSeven.append(newlines[a].pop())
print pdSeven

shuffle(pdSeven)

j = 0
i = 1
template = "Group %d will be %s,%s,%s, and %s."
while(j <len(pdSeven)):
    result = template%(i,pdSeven[j],pdSeven[j+1],pdSeven[j+2],pdSeven[j+3])
    print result
    j = j + 4
    i = i + 1











