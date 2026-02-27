# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Backtracking dengan Prunning (Pemangkasan) | Contoh Backtracking 2 : Kombinasi Biner dengan Batas '1' (Pruning)
#===========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    if jumlah_1 > batas: #Pruning: jika jumlah_1 sudah melewati batas maka berhenti
        return
    
    if len(hasil) == n: #Base case
        print(hasil)
        return
    
    biner_batas(n, batas, hasil + "0", jumlah_1) #Memilih "0"

    biner_batas(n, batas, hasil+"1", jumlah_1+1) #Memilih "1"

biner_batas(4,2)