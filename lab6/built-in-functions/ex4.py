import time
import math

num = float(input())
milli = int(input())
time.sleep(milli/1000)
sqrt_num = math.sqrt(num)
print(f"The square root of {num} after {milli} milliseconds is {sqrt_num}")