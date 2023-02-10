"""
def is_even(num):
  if num % 2 == 0: return True
  return False
"""
def is_prime(num):
  for n in range(2, num):
    if num % n == 0:
      return False
  return True

mylist = [1, 3, 5, 7, 10, 20, 30, 99, 37, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = [x for x in mylist if is_prime(x)]
print(result)