#!/usr/bin/env python
#
# Broadcasts a numpy array from 0 to all the other processes in COMM_WORLD
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD

if comm.rank == 0:
    #rank 0 has data
    A = numpy.arange(10, dtype=numpy.float64)
else:
    #all other have an empty array
    A = numpy.empty(10, dtype=numpy.float64)

# Broadcast from rank 0 to everybody
comm.Bcast( [A, MPI.DOUBLE] , root=0)

print "[%02d] %s" % (comm.rank, A)
