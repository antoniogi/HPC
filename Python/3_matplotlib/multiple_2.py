#!/usr/bin/env python
#
# Creates multiple plots.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import matplotlib.pyplot as plt

def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)


ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0))
ax3 = plt.subplot2grid((3,3), (1,1))
ax4 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
ax5 = plt.subplot2grid((3,3), (2, 0), colspan=2)

make_ticklabels_invisible(plt.gcf())
plt.show()
