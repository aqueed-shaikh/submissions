#!/usr/bin/python

# TO MR. ZAMANSKY: 
# You and I talked about this being commited a little late. I accidentally removed it from the repo instead of moving it last time I commited.
# There should be a record of this existing inside a directory called 'groupinator' under a previous commit (on 9/30).
# Sorry about that! -Will

# Will Field-Thompson & Hunter Herman:

import random

lines = open("students").readlines()

pd6 = [l.strip()[4:] for l in lines if l[0] == '1']
pd7 = [l.strip()[4:] for l in lines if l[0] == '2']

def group(list, gnum):
    ret = []
    random.shuffle(list)
    i = 0
    for item in list:
        print str(gnum) + "," + item
        i += 1
        if (i % 4 == 0):
            gnum += 1

group(pd6, 1)
group(pd7, 9)
