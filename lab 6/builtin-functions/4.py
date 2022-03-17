import time
import math
def root(a) :
    return math.sqrt(a)

a=int(input())
b=int(input())
c=root(a)
time.sleep(b/1000)
print("Square root of", a, "after", b, "miliseconds is", c)