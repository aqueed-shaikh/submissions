#!/usr/bin/python
lines=open("/Users/student/submissions/7/jack_cahn/4-Groupinator/students").readlines()

newlines = []
pd6 = []
pd7 = []

for i in lines:
    newlines.append(i.strip())
    # strip removes the trailing newline
for i in range(0,len(newlines)):
    newlines[i] = newlines[i].split(",")
for i in range(0,len(newlines)):
    if newlines[i][1] == '6':
        pd6.append(newlines[i])
    if newlines[i][1] == '7':
        pd7.append(newlines[i])

for i in range(0,len(newlines)):
    print(str(i/4 + 1) + ',' + newlines[i][2] + ',' + newlines[i][3])
