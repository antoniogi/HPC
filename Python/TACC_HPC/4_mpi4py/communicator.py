#!/usr/bin/env python
#
# Creates a new communicator with half of the processes
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI

world_rank = MPI.COMM_WORLD.rank
world_size = MPI.COMM_WORLD.size

color = world_rank%2
if (color==0):
    key = +world_rank
else:
    key = -world_rank

newcomm = MPI.COMM_WORLD.Split(color, key)

newcomm_rank = newcomm.rank
newcomm_size = newcomm.size
for i in range(world_size):
    MPI.COMM_WORLD.Barrier()
    if (world_rank==i):
      print "Global: rank %d of %d. New comm: rank %d of %d" % (world_rank, world_size, newcomm_rank, newcomm_size)

newcomm.Free()
