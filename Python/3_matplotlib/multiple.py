#!/usr/bin/env python
#
# Creates two charts on the same figure.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def f(t):
  return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, 2.5+np.cos(2*np.pi*t2), color="orange",  linewidth=2.5, linestyle="-")
plt.plot(t2, t2, 'r--')
plt.plot(t2, 5.0-t2, 'g--')
plt.show() 
