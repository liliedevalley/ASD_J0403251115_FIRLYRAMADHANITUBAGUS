# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Latihan 4: Kombinasi Huruf
#===========================================================

def kombinasi(n, hasil=""):
    #Base Case
    if len(hasil) == n: #kalau panjang index hasil sudah sama dengan n
        print(hasil) #mengembalikan hasil
        return
    
    #Recursive Case
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)

#Jumlah kombinasi dihasilkan menggunakan backtracing atau dengan mencoba berbagai kemungkinan seperti pada pohon keputusan
#Fungsi kombinasi ini memiliki rumus 2^n. 2 dihasilkan dari recursive case +"A" dan +"B" (cabang), sedangkan n adalah angka apa yang diminta.
#Sehingga jumlah kombinasi akan dihasilkan berdasarkan jumlah cabang (2) dan kedalaman (n).
#Setiap cabang A dan B akan memiliki 2 kedalaman (karena n nya 2).