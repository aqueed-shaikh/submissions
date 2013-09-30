from random import shuffle

def groupinate(filename):
    with open(filename) as lines:
        return _groupinate(lines)

def _groupinate(lines):
    pd6, pd7 = [], []
    for entry in lines:
        entry=entry.split(",")
        if entry[1]=='6':
            pd6.append(entry[2:4])
        elif entry[1]=='7':
            pd7.append(entry[2:4])
    shuffle(pd6)
    shuffle(pd7)
    pd6 += pd7
    out = []
    for group in range(len(pd6)//4):
        for i in range(4):
            out.append(",".join([str(group+1)]+pd6[4*group+i]))
    return "".join(out)
