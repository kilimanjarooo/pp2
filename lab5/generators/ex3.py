def EUOB(n, a, b):
    for i in range (n+1):
        if i%(a*b) == 0:
            yield i

n = int(input())
a = 3
b = 4

gen = EUOB(n, a, b)

for i in gen:
    print(i)