#!/usr/bin/python


def problemOne():
	sum = 0
	i = 1
	while i < 1000: 
		if i % 3 == 0 or i % 5 == 0:
			sum += i
		i+=1
	print sum

def problemTwo():
	sum = 2
	a = 1
	b = 2
	term = 2 
	while term <= 4000000:
		term = a + b
		a = b
		b = term
		if term % 2 == 0:
			sum += term
	print sum

		
def problemThree():
	answer = 0;
	for first in range (100, 999):	
		for second in range (100, 999):
			product = first * second
			if str(product) == str(product)[::-1]:
				if product > answer:
					answer = product

	print answer

# problemOne()
# problemTwo()
problemThree()
			
