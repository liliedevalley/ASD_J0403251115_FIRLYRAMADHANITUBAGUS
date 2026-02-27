# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Studi Kasus: Generator PIN
#===========================================================

def buat_pin(panjang, hasil=""):
    #Base Case
    if len(hasil) == panjang: #jika panjang index hasil sudah sesuai dengan panjang input
        print(f"PIN: {hasil}") #tampilkan hasil pin
        return #lalu kembalikan
    
    #Recursive Case
    for angka in ["0", "1", "2"]: #setiap angka 0,1,2
        if angka not in hasil: #Kunci Pencegahan, agar mencegah angka berulang (c/: 000, 010, 011, dsb)
            #jika angkanya sudah terpakai maka akan dilewati
            buat_pin(panjang, hasil+angka) 

buat_pin(3)