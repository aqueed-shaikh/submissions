from random import shuffle

lines =open('students').readlines()
p6=[]
p7=[]

for l in lines:
    newlines = l.strip()
    nl=newlines.split(',')
    if nl[1]=='6':
        p6.append(newlines)
    elif nl[1]=='7':
        p7.append(newlines)

shuffle(p6)
shuffle(p7)

for i in range(0,len(p6),4):
    for x in range(0,4):
        p6[i+x]=p6[i+x].split(',')
        p6[i+x][0]=str(i/4)
        p6[i+x].pop(1)
        p6[i+x]=",".join(p6[i+x])
        print p6[i+x]

for i in range(0,len(p7),4):
    for x in range(0,4):
        p7[i+x]=p7[i+x].split(',')
        p7[i+x][0]=str(i/4)
        p7[i+x].pop(1)
        p7[i+x]=",".join(p7[i+x])
        print p7[i+x]
