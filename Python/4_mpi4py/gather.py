#!/usr/bin/env python
#
# Gather example. Every proc sends (rank+1)**2 to 0
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
data = (rank+1)**2
print "[%02d] Sending value: %d " % (rank, data)

data = comm.gather(data, root=0)
if rank == 0:
    for i in range(size):
        assert data[i] == (i+1)**2
else:
    assert data is None

if rank == 0:
    print "[%02d] After gather: %s " % (rank, data)
