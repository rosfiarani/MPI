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
randomangka = random.randint(1,5)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    jumlah = 0
    for i in range(1,size):
        data = comm.recv(source=i, tag=11)
        print(data)
        jumlah += data['send']
    print("Jumlah = ",jumlah)
  
 
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    data = {'rank': rank,'dest':0,'send':randomangka}
    comm.send(data, dest=0, tag=11)