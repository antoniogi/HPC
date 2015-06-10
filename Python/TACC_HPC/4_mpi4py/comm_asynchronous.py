#!/usr/bin/env python
#
# Shows how to use asynchronous communication when irecv is not available
#
#
# agomez (at) tacc.utexas.edu
# 30 Oct 2014
#
# ---------------------------------------------------------------------

from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
assert comm.size == 2

rank = comm.rank
start = MPI.Wtime()
if rank == 0:
    sendmsg = 123
    target = 1
else:
    target = 0

if rank==0:
    time.sleep(2)
    request = comm.isend(sendmsg, dest=target, tag=11)
    request.Wait()
else:
    while not comm.Iprobe(source=target, tag=11):
      print "[%02d] Waiting for message " % rank
      time.sleep (0.5)
    time.sleep(0.5)
    recvmsg = comm.recv (source=target, tag=11)
    print "[%02d] Message received %s " % (rank, str(recvmsg))
comm.Barrier()
end = MPI.Wtime()
if rank==0:
  print "Total time %f" % (end-start)
