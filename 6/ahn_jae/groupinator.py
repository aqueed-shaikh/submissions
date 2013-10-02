# Andrew Zarenberg and Jae Ahn
## Groupinator Improved

import random
import math

lines=open("students").readlines()
newlines = {}
#start from 3 in order to make sure you start at 1 since it starts at 0
i = 3
#make 2 lists
newlines["6"] = [];
newlines["7"] = [];
for l in lines:
#split as per hints
    l = l.strip().split(",")[1:]
    newlines[l[0]].append(l[1:])
#shuffle the groups 6 and 7
random.shuffle(newlines["6"])
random.shuffle(newlines["7"])
for c in newlines:
    for l in newlines[c]:
        i+=1
        l.insert(0,str(math.ceil(i/4)))
        print(",".join(l))
      
    
