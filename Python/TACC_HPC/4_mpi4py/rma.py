#!/usr/bin/env python
#
# One sided communication on mpi4py.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank

n = np.zeros (10, dtype=np.int) # n = [0,0,0,..,0] on all processes
if rank==0:
    win = MPI.Win.Create (n, comm=MPI.COMM_WORLD)
else:
    win = MPI.Win.Create (None, comm=MPI.COMM_WORLD)

if rank==0:
    print "[%02d] Original data %s" % (rank, n)

win.Fence()
if rank!=0:
    data = np.arange(10, dtype = np.int) #creates data=[0,1,...,9]
    win.Accumulate (data, 0, op=MPI.SUM) #adds data+n on proc 0
win.Fence()

if rank==0:
    print "[%02d] Received data %s" % (rank, n)

win.Free()
