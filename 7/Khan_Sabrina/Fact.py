def multiples(n):
    a = 0;
    i = 0;
    while (i<n):
        if(i % 3 == 0 or  i % 5 == 0):
            a = a + i;
        i = i + 1;
    return a

print multiples(10)
print multiples(23)

<<<<<<< HEAD
def fib(n):
    if(n < 1):
        return -1
    a = 1
    b = 1
    c = 2
    if(n == 1 or n == 2):
        return 1
    n = n - 3
    while(n > 0):
        a = b
        b = c
        c = a + b
        n = n - 1
    return c


for i in range(1, 20):
    print str(fib(i)) + " "
=======

def isPrime(n):
    a = 2;
    while(a < n-1):
        if(n % a == 0):
            return False;
        a = a + 1;
    return True;


def largestprime(n):
    a = 0;
    i = n;
    if(i <= 3):
        return i;
    while(i>3):
        if(n % i == 0 and isPrime(i)):
            return i;
        i = i - 1;

print largestprime(13195)
           
>>>>>>> cc0c74d3a62e14707f5a8850b3c4e15bfb193e3a
