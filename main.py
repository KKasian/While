def myfunction(a, b, c):
    while a < b:
        print(a + c)
        a += c
        if a >= b:
            break


myfunction(3 ,15 ,5)
