#Groupinator completed by Justin Duda and Christine Xu

import random

lines = open("students.txt").readlines();

newlines = []

for l in lines: 
  newlines.append( l.strip() )

length = len(newlines)

#print newlines
for i in range(0, length):
 # print l
  newlines[i] = newlines[i].split(",")
  #print l
  newlines[i].pop(0)
  newlines[i].pop(0)

pd6 = []
pd7 = []
groups = []



for i in range (0, length/2):
  pd7.append(newlines.pop())

#print pd7

for i in range (0, length - length/2):
  pd6.append(newlines.pop())

#print "\n"
#print pd6

for i in range (0, 8):
  for g in range (0, 4):
    tmp = [str(i+1)] 
    tmp.extend(pd6.pop(random.randint(0,len(pd6)-1)))
    tmp = ",".join(tmp)
    groups.insert(len(groups)/2, tmp)
    tmp = [str(i+9)]
    tmp.extend(pd7.pop(random.randint(0,len(pd7)-1)))
    tmp = ",".join(tmp)
    groups.append(tmp)

#print groups

#for i in range(0, len(groups)):
  #l.append("\n")
 # newStr = ",".join(groups[i])
  #groups[i] = newStr

groups = "\n".join(groups)

print groups
