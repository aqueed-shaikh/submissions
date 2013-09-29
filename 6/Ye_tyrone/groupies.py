from random import randrange


def access():
    return open('students').readlines()

def edit(lizt):
    newl = []
    for l in lizt:
        if(l[0] == '1'):
            newl.append(l[4:].strip())
    return newl

def randomize(lizt):
    pos = 0
    num = 0
    lef = len(lizt)
    while(pos < lef):
        num = randrange(pos, lef)
        lizt.insert(0,lizt[num])
        del lizt[num + 1]
        pos = pos + 1
    
def labelgrup(lizt):
    group = 1
    no = 1
    for l in lizt:
       print str(group) + "," + l
       no += 1
       if(no > 4):
           group += 1
           no = 1

    

if __name__ == "__main__":
    classed = access()
    #print len(classed)
    classed = edit(classed)
    #print len(classed)
    randomize(classed)
    #print len(classed)
    labelgrup(classed)
    #print classed
    
