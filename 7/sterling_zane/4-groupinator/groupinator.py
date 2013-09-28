#the three-line version
names = [', '.join(line.split(',')[2:]) for line in open('students').read().split('\n')[:-1]
									   if int(line.split(',')[1]) == 7]
x,groups = __import__('random').shuffle(names), [[]]
[groups[-1].append(name) if len(groups[-1]) < 4 else groups.append([name]) for name in names]


#the readable version
#f = open('students')
#text = f.read()

#lines = text.split('\n')[:-1]
#names = []
#for line in lines:
	#line = line.split(',')
	#period = int(line[1])
	#name = ' '.join(line[2:][::-1])

	#if period == 7:
		#names.append(name)
	

#from random import shuffle
#shuffle(names)

#groups = []
#for i in range(int(len(names) / 4)):
	#group = []
	#for j in range(4):
		#group.append(names[i*4 + j])
	#groups.append(group)


for group in groups:
	print group
