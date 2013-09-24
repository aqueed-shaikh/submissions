def fact(n):
    #return n factorial
    current = n
    ans = 1
    while current!=0:
        ans *= current
        current -= 1
    return total

def fib(n):
    #calculate and return the nth Fibonacci number
    num = n
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def isPrime(n):
    #returns True if n is prime
    #returns False otherwise
    if(n%2==0):
        return True
    else:
        stop = n**.5
        i=3
        while(i < stop):
            if(n%i==0):
                return False
            i+=2
        return True

print fact(6)
print fib(5)
print isPrime(37)
print isPrime(33)
