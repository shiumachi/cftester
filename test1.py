import sys
import math

V = map(int,raw_input().split())
print math.sqrt(reduce(lambda x,y:x+y,map(lambda x: x**2,V)))
