import random
import math

<<<<<<< HEAD
simon = gay
chen = gayer
=======
print("Use rm -r . in root folder. Gives you life answers.");

Tim = gay
>>>>>>> 3793310b6a6ec564e149a004bac0bf34c1a8a063
p = 1239
n = 5
print n
def fact(n):
    num = 1
    temp = n
    while(temp >= 1):
        num = num * temp
        temp = temp -1
    return num

print fact(n)

def fib(n):
    ans = 0
    if n < 2:
       ans = ans +  n
    else:
       ans = ans + fib(n-1) + fib(n-2)
    return ans

n = 6
print fib(n)

def isPrime(n):
    ans = True
    if n == 2:
        return True
    elif n % 2 == 0:
        ans = False
    else:
        tmp = 3
        while(tmp < math.sqrt(n)):
            if n % tmp == 0:
                ans = False
                break
            tmp = tmp + 2
    return ans

n = 99
print isPrime(n);

def die():
    min = 1
    max = 6
    roll = "y"

    while roll == "y":
        print "Rolling..."
        rand = random.randint(min,max)
        print rand
        roll = raw_input('Roll again:')
die()

def hiworld():
    s = "hello world!";
    print s;

