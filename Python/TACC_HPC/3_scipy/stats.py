#!/usr/bin/env python
#
# Scipy.stats examples.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import scipy as sp
import numpy as np
s = sp.rand(50)

#Show the mean, variance, std. deviation and the median
mean = sp.mean(s)
std = sp.std(s)
print("Mean : {0:8.6f}".format(mean))
print("Variance : {0:8.6f}".format(sp.var(s)))
print("Std. deviation : {0:8.6f}".format(std))
print("Median : {0:8.6f}".format(sp.median(s)))

from scipy import stats
x = sp.linspace(-3*std, 3*std, 50)
#survival function (probability that the variate has a value greater than the given value
y = stats.norm.sf(x, loc=mean, scale=std)

import matplotlib.pyplot as plt
plt.plot(x,y, color="black")
plt.xlabel("Variate")
plt.ylabel("Probability")
plt.title("SF for Gaussian of mean = {0} & std. deviation = {1}".format(mean, std))
plt.show()
