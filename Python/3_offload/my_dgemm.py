#!/usr/bin/env python
#
# Matrix-matrix multiplication in MATLAB.
# Both matrices here are square ( size x size ).
#
# Intended to demonstrate Automatic Offload to Xeon Phi MIC using
# Intel Math Kernel Library (MKL)
#
# djames (at) tacc.utexas.edu
# cproctor (at) tacc.utexas.edu
# 18 Aug 2014
#
# ---------------------------------------------------------------------

import numpy as np
import time


size      = 8000               # number of rows and columns in each matrix
totalruns = 3                  # total number of runs in this experiment

times     = np.zeros( totalruns )  # times(i) is the time in seconds for run i

print ""
print "  code: Python"
print "  size: %g" % (size)

for run in xrange( totalruns ):
  
  print ""
  print "\t------------------------"
  print "\t ...executing run %g... " % ( run )
  print "\t------------------------"
  print ""

  # Initialize matrices for new run.  Remember that a NumPy matrix, a NumPy array,
  # and a Python array are all different things.   Here we're using NumPy matrices;
  # for NumPy matrices, the "*" operator does matrix multiplication by calling
  # BLAS.  (With arrays, the "*" operator generally gives you element-by-element
  # multiplication, and does not use BLAS.)

  A = np.matrix( np.random.random( (size, size) ) )  # CAUTION: SEE COMMENTS ABOVE
  B = np.matrix( np.random.random( (size, size) ) )  # CAUTION: SEE COMMENTS ABOVE

  # Multiply...

  start_time = time.time()                           # alternative: time.clock()
  C = A*B                                            # CAUTION: SEE COMMENTS ABOVE
  end_time = time.time()
  times[ run ] = end_time - start_time

  # Clear matrices...

  del A
  del B
  del C

# end run loop


# Report times for each run...

print ""
print "  code: Python"
print "  size: %g" % (size)
print ""

for run in xrange( totalruns ):
  print "                      run %g time: %.2f sec" % ( run, times[run] )

# Compute and display overall average time...

avgtime = np.average( times )

print ""
print "         average time (all runs): %.2f sec" % ( avgtime )

# Compute and display overall average time excluding first run...

avgtime = np.average( times[1:len(times)] )

print "     average time (skip 1st run): %.2f sec" % ( avgtime )
print ""

