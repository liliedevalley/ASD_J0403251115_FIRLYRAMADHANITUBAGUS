# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Konsep Dasar Backtracking | Contoh Backtracking 1 : Backtracking Kombinasi Biner
#===========================================================

def biner(n, hasil=""):
    if len(hasil) == n: #base case: jika panjang string sudah n, cetak hasilnya
        print(hasil)
        return
    
    biner(n, hasil + "0") #choose + explore: tambah '0'

    biner(n, hasil + "1") #choose + explore: tambah '1'

biner(3)