#!/usr/bin/env python
#
# Multiple ways of defining arrays with numpy.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import numpy as np
a = np.array([2, 3, 12])  # Create from list
a = np.arange(10)      # 0, 1, 2, 3, 4,..., 9
b = np.arange (0,10,2) # start, end (exclusive), step. 0, 2, 4, 6, 8
#By number of points (start, end, num. points)
a = np.linspace(0,1,5) #0, 0.25, 0.50, 0.75, 1.0
a = np.linspace(0,1,5,endpoint=False) #0, 0.2, 0.4, 0.6, 0.8
#Useful arrays
a = np.ones((4,4))
a = np.zeros((3,3))
a = np.diag(np.ones(3))
a = np.eye(3)
#with random numbers
np.random.seed(1111)   #sets the random seed
a = np.random.rand(4)  #uniform in [0,1]
b = np.random.randn(4) #Gaussian
#uninitialized
a = np.empty((3,3))
#resize
a = np.zeros(10)
a = np.resize(a, 20)
