def even(N):
    for i in range (N+1):
        if i%2 == 0:
            yield i

n = int(input())
gen = even(n)

nums = []
for i in gen:
    nums.append(str(i))

output = ", ".join(nums)

print(output)