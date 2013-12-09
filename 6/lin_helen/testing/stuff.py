from random import randrange


def function(a, b):
    print("This is quite a cool function.")
    g = str(a + randrange(0, 100) * b)
    print("I know where you live.\nYou live on %s Street.") % (g)


def helen():
    print("You're %d percent less cool than I am.") % randrange(0,100)

function(1, 2)
helen()
