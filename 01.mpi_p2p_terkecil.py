# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    data = 'hello from '+str(rank)
    for i in range(size):
        if i != rank:
            comm.send(data,dest=i,tag=3)
    print("rank terkecil =",rank)

# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    data = comm.recv(source=0,tag=3)
    print("hello rank",rank,",you get message --->",data)
	
