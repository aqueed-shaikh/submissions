"""
groupinator.py reads the students file, which contains "classnumber,period,
surname,firstName" of every Software Development student, and prints randomized
groups of four students (by class).

Note: the application is not scalable: many values are hard-coded.
"""

from random import shuffle

students = open("students").readlines()
students = [student.strip() for student in students]
students6 =	students[:32]
students7 = students[32:]

shuffle(students6)
shuffle(students7)

for group in range(8):
	for individual in range(4):
		print "%d,%s" % (group, students6[group * 4 + individual][4:])

for group in range(8):
	for individual in range(4):
		print "%d,%s" % (group + 9, students7[group * 4 + individual][4:])
