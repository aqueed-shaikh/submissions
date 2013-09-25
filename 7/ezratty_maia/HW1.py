def fact(n):
    # return n factorial
    if n==1:
        return 1
    return n * fact(n-1)

def fib(n):
    # calculate and return the nth Fibonacci number
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

print fib(4)
print fact(3)
    

    #def isPrime(n):
     #returns True (which is a value in Python) if n is prime
     # returns False otherwise (which is also a value)
     #For the isPrime, the easiest way is to check to see if n is evenly divisible by any integer smaller than n and larger than 2 but there are much better ways as well.
    
