#!/usr/bin/env python
#
# Iterative example to show Cython capabilities.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from libc.math cimport sqrt
#cdef extern from "math.h":
#  double sqrt(double x)

cdef double f(double arg):
  cdef double res = 0.0
  cdef int i = 0
  for i in range(50000000):
    res+=sqrt((i+1)*arg**5)
  return res

def function(double arg):
  return f(arg)
