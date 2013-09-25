def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fact(n):

    if n == 1: return n
    else:
        return n * fact(n - 1)
def isPrime(n):

    n = abs(int(n))
    if n < 2:
        return "false"
    if n == 2:
        return "true"
    for x in range(2, n-1): 
        if n % x == 0:
            return "false"
        else:
            return "true"
print fib(8)
print fact(8)
print isPrime(8)

