#!/usr/bin/python

from math import sqrt, floor

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def isPrime(n):
    if n%2 == 0:
        return False
    x = floor(sqrt(n))
  #  return x
    while x > 1:
        if n%x == 0:
            return False
        if x == 2:
            return True
        x = x-1

def oddSum(n):
    if n == 1:
        return 1
    if n%2 == 0:
        return oddSum(n-1)
    else:
        return n + oddSum(n-2)

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)

        
