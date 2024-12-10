# Membuat list 
kota = ["padang","jakarta","palembang","bandung","bogor"]
huruf = ["a","b","c","d","e"]

angka = [1,2,3,4,5]
# menampilkan list 
print("List kota :",kota)
print("List huruf :",huruf)
print("List angka :",angka)

# mengakses nilai dalam list
kota = ["padang","jakarta","palembang","bandung","bogor"]
# mengakses nilai palebang 
print(kota[2],"ada pada indeks ke 2")
# memperbarui nilai 
kota = ["padang","jakarta","palembang","bandung","bogor"]
print ("list kota awal ",kota)

kota[1] ="cilacap"
print ("list kota baru ",kota)
# menghapus nilai dalam list
kota = ["padang","jakarta","palembang","bandung","bogor"]
print ("list kota awal ",kota)

del kota[1]
print ("list kota baru ",kota)
