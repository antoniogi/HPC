#!/usr/bin/env python

#Trivial example of how to implement a generator in Python
def my_range(start, end):
  current = start
  while current<end:
    yield current
    current += 1

for i in my_range (10, 20):
  print i
  
