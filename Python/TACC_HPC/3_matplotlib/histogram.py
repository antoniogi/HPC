#!/usr/bin/env python
#
# Creates and displays a histogram.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
# make an array of random numbers with
#a gaussian distribution with
# mean = 5.0
# rms = 3.0
# number of points = 1000
data = np.random.normal(5.0, 3.0, 1000)
# make a histogram of the data array
plt.hist(data)
# make plot labels
plt.xlabel("data")
plt.show() 
