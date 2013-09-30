lines = open("students").readlines()
newlines = []
for l in lines: newlines.append(l.strip())
print newlines
newerlines=[]
for i in newlines:newerlines.append(i.split(","))
print newerlines
