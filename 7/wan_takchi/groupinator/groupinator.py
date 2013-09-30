import random

lines = open("students.txt").readlines()
p6=[]
p7=[]
for l in lines: 
  newlines = l.strip()
  spli=newlines.split(",")
  if spli[1]=="6":
    p6.append(newlines)
  else
    p7.append(newlines)
random.shuffle(p6)
random.shuffle(p7)
