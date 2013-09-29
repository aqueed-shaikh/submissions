def fact(n):
    if n>0:
	return n + fact(n-1)
    else:
	return 0

def fibh(n, x, y):
    if n > 0:
	return fibh(n - 1, y, x+y)
    else:
	return x + y

def fib(n):
    if n == 0:
	return 1
    elif n == 1:
	return 1
    else:
	return fibh(n-2, 1, 1)

def isPrimeh(n, t):
    if t == n:
	return True
    elif n % t == 0:
	return False
    else:
	return isPrimeh(n, t + 1)

def isPrime(n):
    return isPrimeh(n, 2)

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def nameScore(name):
    l = list(name)
    score = 0
    for x in l:
	score = score + a.index(x) + 1
    return score

name = raw_input('Please enter your name in lower case \n')

print '\nHi,', name,'! your Name Score is . . . ', nameScore(name), '!!'
