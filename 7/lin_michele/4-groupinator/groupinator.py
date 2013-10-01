import random
def groupinator():
    lines = open("students").readlines()
    pd6 = []
    pd7 = []
    groups = []
    for l in lines:
        l = l.strip()
        l = l.split(",")
        if (l[0] == "1"):
            pd6.append(l[2:])
        else:
            pd7.append(l[2:])
    random.shuffle(pd6)
    random.shuffle(pd7)
    i = 0
    j = 1
    k = 0
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
    for l in groupinator():
        l = ", ".join(l);
        print l
