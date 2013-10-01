import random

def readFile(filename):
	Text = open (filename,"r")
	Text = Text.readlines()
	List = []
	for Line in Text:
		List.append(Line.strip())
	return List

#print readFile("students.txt")
List = readFile("students.txt")
Class6 = []
Class7 = []
for element in List:
	if (element[:1] == "1"):
		Class6.append(element[4:])
	else:
		Class7.append(element[4:])
#print L1
#print L2
"""If you want the lists randomized it should be done here.
Shuffle the lists or something.
"""
num = 1
runs = 0
elementno = 0
for element in Class6:
	if(runs == 4):
		runs = 0
		num += 1 
	Class6[elementno] = str(num) + "," + element
	runs += 1
	elementno += 1
elementno = 0
for element in Class7:
	if(runs == 4):
		runs = 0
		num += 1 
	Class7[elementno] = str(num) + "," + element
	runs += 1
	elementno += 1
#print Class6
#print Class7
End = Class6 + Class7
#print End
for element in End:
	print(element) #+ "\n")
	
	
