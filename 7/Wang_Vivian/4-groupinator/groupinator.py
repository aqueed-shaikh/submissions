import random

def groupinator():
    f = open("students.txt",'r')
    r = f.read()
    lines = r.split("\n")
    i = lines.index("")
    if (i > -1 and i < 65):
        lines.remove("")
    pd6 = lines[:32]
    pd7 = lines[32:]
    random.shuffle(pd6)
    random.shuffle(pd7)
    sort(pd6,4)
    sort(pd7,36)
    show(pd6)
    show(pd7)


def sort(x,i):
    for a in range(len(x)):
        x[a] = str(i/4) + x[a][3:]
        i += 1

def show(x):
    for a in x:
        print a

groupinator()
