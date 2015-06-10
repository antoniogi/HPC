#!/usr/bin/env python
#
# Shows how to use the Request class to create asynchronous communication.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

if rank==0:
    requests = [MPI.REQUEST_NULL for i in range(0,size)]
    d = np.zeros (size, dtype='i')
    print "[%02d] Original data %s " % (rank, d)
    #Request data from a set of processes
    for i in range (1, size):
        requests[i] = comm.Irecv([d[i:],1, MPI.INT], i, MPI.ANY_TAG)

    status = [MPI.Status() for i in range(0,size)]
    #Wait for all the messages
    MPI.Request.Waitall(requests, status)
    for i in range(1,size):
        source = status[i].source
        tag = status[i].tag
        assert d[i] == source ; assert d[i] == tag
    print "[%02d] Received data %s " % (rank, d)
else:
    data = np.array ([rank])
    time.sleep (np.random.random_sample())
    request = comm.Isend ([data[:], 1, MPI.INT] , 0, rank)
    request.Wait()
comm.Barrier()
