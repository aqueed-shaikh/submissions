def listLength(lista):
    i = 0
    for l in lista:
        i += 1
    return i

def clearList(lista):
    i = 0
    l = listLength(lista)
    while (i < l):
        lista.pop()
        i += 1
