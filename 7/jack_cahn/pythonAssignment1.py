#!/usr/bin/python

def fact(n):
    if n==1:
        return 1; 
    else: 
        return n * fact(n-1); 

#print(fact(5));

def fib(n):
    if n==1:
        return 0; 
    if n==2: 
        return 1; 
    else: 
        return fib(n-1) + fib(n-2); 

#print(fib(5)); 

def isPrime(n):
    a = 2; 
    while a < n: 
        if n%a == 0:
            return False; 
        else: 
            a = a + 1; 
    return True; 

print(isPrime(10)); 
