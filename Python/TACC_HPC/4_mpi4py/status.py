#!/usr/bin/env python
#
# Basic example to show the functionality of the Status class.
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
assert comm.size == 2

rank = comm.rank
status = MPI.Status()

# pass explicit MPI datatypes
if rank == 0:
    data = numpy.arange(1000, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank == 1:
    data = numpy.empty(1000, dtype='i')
    comm.Recv([data, MPI.INT], source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
    source = status.Get_source()
    tag = status.Get_tag()
    print "[%02d] Received data from source %d with tag %d" % (rank, source, tag)
