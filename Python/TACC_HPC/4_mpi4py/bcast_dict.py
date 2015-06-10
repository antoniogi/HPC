#!/usr/bin/env python
#
# Broadcasts a dictionary from 0 to all the other processes in COMM_WORLD
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI

comm = MPI.COMM_WORLD

if comm.rank == 0:
    data = {'key1' : [7, 2.72, 2+3j],
           'key2' : ( 'abc', 'xyz')}
else:
    data = None

data = comm.bcast(data, root=0)
print "[%02d] %s" % (comm.rank, data)
