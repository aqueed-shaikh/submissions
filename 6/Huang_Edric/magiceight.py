import sys
import random
 
ans = True
 
while ans:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
     
    answers = random.randint(1,8)
     
    if question == "":
        sys.exit()
     
    elif answers == 1:
        print "It is certain!!!!!!!!!!!!!1"
     
    elif answers == 2:
        print "Signs point to yes!!!!!"
     
    elif answers == 3:
        print "You may rely on it!"
     
    elif answers == 4:
        print "Ask again later. Best advice I could give."
     
    elif answers == 5:
        print "Concentrate and ask again bud"
     
    elif answers == 6:
        print "Better not tell you now..."
     
    elif answers == 7:
        print "Don't count on it. Go away."
     
    elif answers == 8:
        print "My sources say no. Sorry not sorry."
