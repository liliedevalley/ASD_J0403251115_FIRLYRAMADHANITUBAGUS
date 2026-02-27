# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Latihan 3: Mencari Nilai Maksimum
#===========================================================

def cari_maks(data, index=0):
    #Base case
    if index == len(data)-1: #jika indexnya sudah sama dengan panjang data yang dikurangi 1
        return data[index] #kembalikkan data dengan index tsb
    
    #Recursive case
    maks_sisa = cari_maks(data, index+1)

    if data[index] > maks_sisa: #jika data dengan indeks tsb lebih besar dari nilai maks sisa
        return data[index] #kembalikan data dgn indeks tsb
    else:
        return maks_sisa #jika tidak maka kembalikan nilai maks_sisa
    
angka = [3,7,2,9,5]
print(f"Nilai maksimum: {cari_maks(angka)}")

#Alur Program
#Mulai memanggil index pertama sampai ke index terakhir yang dikurangi satu
#index=0 → panggil index=1
#index=1 → panggil index=2
#index=2 → panggil index=3
#index=3 → panggil index=4
#Karena index ke-4 merupakan len(data)-1 maka masuk ke Base Case dan mengembalikkan data index tersebut data[4]=5
#Lalu mulai membandingkan nilai maks_sisa dengan data[index]
#data[3]=9
#maks_sisa=5
#9>5 maka return 9
#begitu seterusnya sampai index[0]