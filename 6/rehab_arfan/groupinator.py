#Arfan Rehab, Derek Tang

import random

def groupinator():
    lines = open("students").readlines()
    pd6 = []
    pd7 = []
    groups = []

    for temp in lines:
        temp = temp.strip()
        temp = temp.split(",")
        if (temp[0] is "1"):
            pd6.append(temp[2:])
        else:
            pd7.append(temp[2:])

    random.shuffle(pd6)
    random.shuffle(pd7)

    i = 0
    j = 1
    k = 0

    #for period 6 groups
    #8 groups in total
    while j < 9:
        pd6[k].insert(0,str(j))
        groups.append(pd6[k])
        i += 1
        k += 1
        if i == 4:
            i = 0
            j += 1

    k = 0
    i = 0

    #for period 7 groups
    while j < 17:
        pd7[k].insert(0,str(j))
        groups.append(pd7[k])
        i += 1
        k += 1
        if i == 4:
            i = 0
            j += 1
    return groups

if __name__ == "__main__":
    for temp in groupinator():
        temp = ",".join(temp);
        print temp
