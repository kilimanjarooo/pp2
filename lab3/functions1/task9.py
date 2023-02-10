import math

def Volume(r):
  return (4/3) * (math.pi) * pow(r,3)

R = int(input())

print(Volume(R))