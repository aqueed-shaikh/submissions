from random import randrange


def function(a, b):
    print("This is a cool function.")
    g = str(a + randrange(0, 100) * b)
    print("I know where you live.\nYou live on %s Street.") % (g)

function(1, 2)
