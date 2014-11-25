#!/usr/bin/env python
#
# Creates and displays a bar plot.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
yvals = [-100, 200, -25, 50, 10]
bars = plt.bar(x, yvals)  #specifies we are using a bar chart
plt.xticks(x+0.5, ('x1', 'x2', 'x3', 'x4', 'x5'))
plt.show()
