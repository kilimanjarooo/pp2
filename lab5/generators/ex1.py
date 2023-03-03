def squares(N):
    for i in range (N+1):
        yield i**2

n = int(input())
gen = squares(n)

for i in range (n+1):
    print(next(gen))