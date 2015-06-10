#!/usr/bin/env python
#
# Creates and displays a bar plot. Changes the bar color depending on
# the y value
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
bars = plt.bar(x, yvals)

#change color of bars when y<0
for idx, val in enumerate(yvals):
  if (val<0):
    bars[idx].set_color('r')

plt.xticks(x+0.5, ('x1', 'x2', 'x3', 'x4', 'x5'))

#add a horizontal line at y=0
plt.axhline(0, color='black')
plt.show()
