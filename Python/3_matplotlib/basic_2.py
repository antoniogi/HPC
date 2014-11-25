#!/usr/bin/env python
#
# Add some more detail to the basic plot with two series.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
#add a title
plt.title('This is a title')
#get the individual plots
plt1, = plt.plot([1,2,3,4,5,6],'o')
plt2, = plt.plot([6,5,4,3,2,1])
#add the legend
plt.legend ([plt1, plt2], ['blue circles', 'green line'])

plt.ylabel('y label')
plt.xlabel('x label')
plt.show()
