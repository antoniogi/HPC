#!/usr/bin/env python
#
# Iterative example to show Cython capabilities.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import math

def function(double arg):
    cdef double res = 0.0
    for i in range(50000000):
        res+=math.sqrt((i+1)*arg**5)
    return res

