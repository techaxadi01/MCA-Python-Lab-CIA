import math

print(math.sqrt(25))
print(math.pow(2,3))
print(math.pi)


from math import factorial

print(factorial(6))

import math as m 

print(m.sin(90))
print(m.sin(m.pi/2))

import statistics as s

print (s.mean([1,5,1,9,6,5,4,8,5,]))

from statistics import *

marks = [1,5,1,9,6,5,4,8,5,]

print("Average marks: ",mean(marks))
print("Median: ",median(marks))
print("std: ",stdev(marks))