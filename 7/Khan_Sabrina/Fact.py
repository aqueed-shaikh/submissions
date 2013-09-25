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

