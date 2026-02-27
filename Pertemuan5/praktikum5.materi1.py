# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Konsep Dasar Rekursif | Contoh Rekursi 1 : Faktorial
#===========================================================

def faktorial(n):
    if n == 0: #Base case: berhenti ketika n = 0
        return 1
    
    return n * faktorial(n-1) #Recursive case: masalah diperkecil menjadi faktorial(n-1)
print(faktorial(5)) #Menampilkan outpu: 120
print(faktorial(8))