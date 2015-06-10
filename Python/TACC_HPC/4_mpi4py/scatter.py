#!/usr/bin/env python
#
# Scatter example using mpi4py.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

if rank == 0:
    data = [i for i in range(size)]
    print "[%02d] Original data: %s" % (rank, data)
else:
    data = None
data = comm.scatter(data, root=0)
assert data == rank

print "[%02d] Data received: %d" % (rank, data)
