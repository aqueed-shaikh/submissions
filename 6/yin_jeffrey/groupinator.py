import random
import csv
results = csv.writer(open("groups.csv","wb"))
lines=open("students").readlines()
newlines=[]
for l in lines: 
    if l[2:3]=='6':
        newlines.append(l.strip()[4:])
random.shuffle(newlines)
i=1
for l in newlines:
    results.writerow([str(i/5+1) + "," + l])
    print str(i/5 + 1) + "," + l
    i= i+1

#Results will be in a file called groups.csv
#further note: do not run in a folder where you already have groups.csv
# or you will be sad
