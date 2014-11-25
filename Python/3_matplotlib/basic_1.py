#!/usr/bin/env python
#
# Very basic plot with two series.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5,6],'o')
plt.plot([6,5,4,3,2,1])
plt.ylabel('y label')
plt.xlabel('x label')
plt.show()
#replace `plt.show()` by 
#plt.savefig('basic1.png')
