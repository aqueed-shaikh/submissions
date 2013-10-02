import csv
import random

def readList ():
    lines=open("/Users/student/Dropbox/Classes/Grade_12/Software_Development/submissions/6/Cahn_David/students").readlines()
    period6 = []
    period7 = []
    groupNum = 1
    counter1 = 0
    counter2 = 0

    for lineNum in lines:
        if lineNum [0] == "1":
            x =  len (lineNum)
            substring = lineNum [4: x-1]
            period6.append (groupNum)
            period6.append (substring)
            counter1 = counter1 + 1;
            if counter1 % 4 == 0:
                groupNum = groupNum + 1
        else:
            x =  len (lineNum) 
            substring = lineNum [4:x-1]
            period7.append(groupNum)
            period7.append(substring)
            counter2 = counter2 + 1;
            if counter2 % 4 == 0:
                groupNum = groupNum + 1

    return [period6, period7]
    
def main ():
    ans = readList ()
    period6 = ans [0]
    period7 = ans [1]

    print "PRINTING PERIOD 6 GROUPS"
    print period6

    print "PRINTING PERIOD 7 GROUPS"
    print period7


if __name__ == "__main__":
    main()

    
            
