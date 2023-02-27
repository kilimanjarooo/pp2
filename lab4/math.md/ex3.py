from math import *
import math

def area(n, s):
    return (n*pow(s,2))/(4*tan(math.pi/n))

print ("write number of sides:", end=" ")
n = int(input())

print ("write the length of a side:", end=" ")
s = int(input())

print("area of regulat polygon =", area(n, s))