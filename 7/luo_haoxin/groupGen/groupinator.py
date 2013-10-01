from random import shuffle

def groupGen():
    pd6 = []
    pd7 = []
    period6 = ""
    period7 = ""
    
    lines = open("students").readlines()
    for l in lines:
        plhold = l.split(",")
        if plhold[1] =="6":
            plhold = ",".join(plhold[2:])
            pd6.append(plhold)
        else:
            plhold = ",".join(plhold[2:])
            pd7.append(plhold)
  
    shuffle(pd6)
    shuffle(pd7)

    for i in range(0,len(pd6)):
        val = "%d,"
        period6+= val %(i/4 + 1) + pd6[i]
        period7+= val %(i/4 + len(pd6)/4 + 1) + pd7[i]
    ans = period6 + period7
    print ans

if __name__ == "__main__":
    groupGen()
