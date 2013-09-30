import random

lines = open("students").readlines()
p6=[]
p7=[]
for l in lines:
  newlines = l.strip()
  spli=newlines.split(",")
  if spli[1]=="6":
    p6.append(newlines)
  else:
    p7.append(newlines)
random.shuffle(p6)
random.shuffle(p7)
bothpd = p6+p7

def makegroups():
    groups = ""
    i=0
    while len(bothpd)>0:
        groups+= (str)(i/4+1) + "," + bothpd.pop() + "\n"
        i+=1
    return groups

print makegroups()
