from random import shuffle

lines =open('students').readlines()
p6=[]
p7=[]
#groups=[]

for l in lines:
    newlines = l.strip()
    nl=newlines.split(',')
    #groups.append(newlines)
    if nl[1]=='6':
        p6.append(newlines)
    elif nl[1]=='7':
        p7.append(newlines)

shuffle(p6)
shuffle(p7)
g=p6+p7

for i in range(0,len(g),4):
    for x in range(0,4):
        g[i+x]=g[i+x].split(',')
        g[i+x][0]=str(i/4+1)
        g[i+x].pop(1)
        g[i+x]=",".join(g[i+x])
        print g[i+x]
