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
           
