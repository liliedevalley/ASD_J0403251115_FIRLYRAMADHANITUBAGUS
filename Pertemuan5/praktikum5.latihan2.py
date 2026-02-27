# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Latihan 2: Tracing Rekursi
#===========================================================

def countdown(n):
#Menghitung mundur angka
    #Base case
    if n == 0: #jika angka sudah sampai 0 maka print selesai dan return
        print("Selesai")
        return
    print(f"Masuk: {n}") #setiap angka yang masuk ditampilkan

    #Recursive case
    countdown(n-1) #angka yang ingin dihitung mundur dikurangi 1
    print(f"Keluar: {n}") #setiap angka yang keluar ditampilkan

countdown(3)
#Output muncul terbalik karena dia termasuk LIFO (Last In, First Out) ditunda sampai pemanggilan fungsi rekursif selesai,
#print(f"keluar: {n}") akan dieksekusi saat fase dibongkar atau unwinding.
#Jadi dikerjakan dari dalam dulu
#angka 3 masuk -> (rekursif) angka 2 masuk -> (rekursif) angka 1 masuk -> (n suudah sama dengan 0 maka print selesai) -> (base case angka 1) angka 1 keluar -> (base case angka 2) angka 2 keluar -> (base case) angka 3 keluar