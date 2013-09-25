import random


total_fear = 0

for x in range(0, random.randrange(1, 999)):
    print "I AM HERMAN NUMBER %i HEAR ME ROAR"%(x*x)
    num = random.randrange(100, 450)
    print "fear level: %i"%num
    total_fear += num

print "meow. total fear: %i"%total_fear    



