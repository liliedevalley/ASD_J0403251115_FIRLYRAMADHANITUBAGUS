#========================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1: Membaca seluruh isi file data
#========================================================================

#membuka file dalam satu string
print("===Membuka file dalam satu string===")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #mengambil semua data dan disimpan di 1 variabel
print(isi_file)
print(f"tipe data: {type(isi_file)}")

# membuka file perbaris
print("===Membuka file perbaris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris #gunakan .strip jika ingin menghapus garis baru
        print(f"Baris ke: {jumlah_baris}")
        print(f"isinya: {baris}")


#========================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Parsing Data
#========================================================================

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baur
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print(f"NIM : {nim} | NAMA : {nama} | Nilai : {nilai}")


#========================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3: Membaca Data dan Menyimpannya ke Struktur Data List
#========================================================================

data_list = [] #inisialisasi list dalam menampung data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baur
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim, nama, int(nilai)]) #proses menyimpan data ke dalam list
print("=== Menampilkan List===")
print(data_list)
print(f"Contoh record pertama: {data_list[0]}")
print(f"Contoh record terakhir: {data_list[9]}")
print(f"Jumlah data record: {len(data_list)}")

#========================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4: Membaca Data dan Menyimpannya ke Struktur Data Dictionary
#========================================================================

data_dict = {} #inisialisasi dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baur
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        data_dict[nim] = { #simpan ke dalam dictionary
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("=== Menampilkan Dictionary===")
print(data_dict)