# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()


# generate angka integer secara random untuk setiap proses
val = random.randint(10,100)
print ("Rank %d/%d has value %d" %(rank, size, val))
# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
sum = comm.reduce(val, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank == 0:
    print ("Rank 0 got the sum, the total is %d" %sum)

