from random import shuffle

lines = open('students').readlines()
newlines = []
for l in lines: 
    newlines.append(l.strip().split(","))

pd6 = []
pd7 = []

for l in newlines:
    if l[0] == '1':
        pd6.append(l)
    else:
        pd7.append(l)

shuffle(pd6)
shuffle(pd7)

for i in range(0,8):
    print "%i,%s,%s"%(i+1,pd6[4*i][2],pd6[4*i][3])
    print "%i,%s,%s"%(i+1,pd6[4*i+1][2],pd6[4*i+1][3])
    print "%i,%s,%s"%(i+1,pd6[4*i+2][2],pd6[4*i+2][3])
    print "%i,%s,%s \n"%(i+1,pd6[4*i+3][2],pd6[4*i+3][3])

for i in range(0,8):
    print "%i,%s,%s"%(i+9,pd7[4*i][2],pd7[4*i][3])
    print "%i,%s,%s"%(i+9,pd7[4*i+1][2],pd7[4*i+1][3])
    print "%i,%s,%s"%(i+9,pd7[4*i+2][2],pd7[4*i+2][3])
    print "%i,%s,%s \n"%(i+9,pd7[4*i+3][2],pd7[4*i+3][3])

