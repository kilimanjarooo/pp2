def my_func(n):
  return lambda a : a * n
mydoubler = my_func(2)

print(mydoubler(11))