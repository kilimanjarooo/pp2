from itertools import permutations
slovo = str(input())
perms = [''.join(p) for p in permutations(slovo)]
print(perms)