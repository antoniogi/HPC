#!/usr/bin/env python
#
# Creates and displays a box plot.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
#gaussian distributions
dataset_1 = np.random.normal(5.0, 3.0, 1000)
dataset_2 = np.random.normal(5.0, 5.0, 1000)
dataset_3 = np.random.normal(4.0, 1.0, 1000)
data=[dataset_1, dataset_2, dataset_3]
plt.xticks( np.arange(3), ("Dataset 1", "Dataset 2", "Dataset 3") )
plt.boxplot(data)
plt.show() 
