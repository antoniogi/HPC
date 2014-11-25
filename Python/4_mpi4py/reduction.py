#!/usr/bin/env python
#
# Reduction example.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

import numpy as np 
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank 

#Give me my start and end index of an array of size N using my rank
def partition(rank, size, N): 
    n = N//size + ((N % size) > rank) 
    s = rank * (N//size) 
    if (N % size) > rank: 
        s += rank 
    else: 
        s += N % size 
    return s, s+n 

#Define the size of the problem
N = 1000
start, end = partition(rank, size, N) 

#Calculate the local sum of all the integers from start to end
local_sum = sum(range(start,end))
#Get the global sum
global_sum = comm.reduce (local_sum, op=MPI.SUM, root=0)
if rank == 0: 
    print "[%02d] Received: %d -- Correct: %d" % (rank, global_sum, np.arange(N).sum())
