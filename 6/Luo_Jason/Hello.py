#!/usr/bin/python

def fact (n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print fact (5)

def fib (n):
    count = 0
    if n == 1:
        return count + 0
    elif n == 2:
        return count + 1
    else:
        return count + fib(n-1) + fib(n-2)

print fib(10)

def isPrime(n):
    last = False
    if n % 2 == 0:
        return not last
    return last

print isPrime(3)
    
