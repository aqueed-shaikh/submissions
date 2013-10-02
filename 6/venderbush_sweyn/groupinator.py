#!/usr/bin/python

import csv
import random

#Returns a list of a list of class1 students and a list of class2 students
def shuffledLists(file="/Users/sweyn/Dropbox/School/SoftDev/classcode/resources/groupinator/students"):
    file = open(file)
    read = csv.reader(file)

    students1 = []
    students2 = []

    for row in read:
        if row[0] == "1":
            students1.append(row)
        else:
            students2.append(row)

    random.shuffle(students1)
    random.shuffle(students2)

    return [students1,students2]

#Pre: takes a list of 2 lists, one of each class
#Post: returns a list of lists, one for each group
def makeGroups(studentsList):
    groups = []
    groupnum = 1
    for classStudents in studentsList:
        classGroups = []
        for studnum in range(0,len(classStudents), 4):
            group = []
            for student in range(0,4):
                group.append([groupnum,classStudents[studnum+student][2], classStudents[studnum+student][3]])
            classGroups.append(group)
            groupnum += 1
        groups.append(classGroups)
    return groups

#Prints each member of each group in order
def printGroups(groupList):
    for eachclass in groupList:
        for group in eachclass:
            for member in group:
                print "%s,%s,%s" % (str(member[0]), member[1], member[2])

def main():
    studentsList = shuffledLists()
    groupList = makeGroups(studentsList)
    printGroups(groupList)

if __name__ == "__main__":
    main()


