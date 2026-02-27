# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Rekursi pada Data List | Contoh Rekursi 3 : Menjumlahkan Elemen List
#===========================================================

def jumlah_list(data, index=0):
    if index == len(data): #Base case: jika index sudah mencapai panjang list
        return 0
    
    return data[index] + jumlah_list(data,index+1) #Recursive case: elemen sekarnag + jumlah elemen setelahnya

print(jumlah_list([2,4,6,8])) #Menampilkan Output 20