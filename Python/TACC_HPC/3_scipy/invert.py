#!/usr/bin/env python
#
# How to invert a numpy 2 dimensional array with scipy.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from scipy import linalg
import numpy as np

arr = np.arange (4).reshape((2,2))
print arr
iarr = linalg.inv(arr)
print iarr
