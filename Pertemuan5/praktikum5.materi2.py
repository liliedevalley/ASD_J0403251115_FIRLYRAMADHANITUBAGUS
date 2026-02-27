# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Tracing Rekursi | Contoh Rekursi 2 : Tracing Masuk/Keluar
#===========================================================

def hitung(n):
    if n == 0: #Base case, jika n sudah habis maka berhenti
        print("Selesai")
        return
    print(f"Masuk: {n}") #fase stacking
    print(n-1) #pemanggilan rekursif
    print(f"Keluar {n}") #fase unwinding

hitung(3)