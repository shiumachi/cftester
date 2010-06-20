#!/usr/bin/python
import sys
import math

V = map(int,raw_input().split())
if V[0] == -2: 
    print 0
    exit()
print math.sqrt(reduce(lambda x,y:x+y,map(lambda x: x**2,V)))

