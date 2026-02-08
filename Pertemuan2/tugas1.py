# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#------------------
#variabel nama file
nama_file = "data_barang.txt"
#------------------

#------------------
#fungsi 1: membaca data dari file
#------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks dengan format: kodebarang, namabarang, stok
    """

    stock_dict = {} #menginisialisasi data dictionary
    with open(nama_file, "r", encoding= "utf-8") as file:
        for baris in file:
            baris = baris.strip() #strip untuk menghapus whitespace diakhir
            KodeBarang, NamaBarang, Stok = baris.split(",") #memecah data menjadi satuan dan menyimpan ke dalam variabel
            stock_dict[KodeBarang] = { #menyimpan data ke dalam dictionary
                "Nama Barang" : NamaBarang,
                "Stok Barang" : int(Stok)
            }
        return stock_dict
    
#------------------
#fungsi 2: menampilkan semua data
#------------------
def tampilkan_semua(stok_dict):
    """Menampilkan semua barang yang ada di stok_dict"""
    #membuat header tabel
    print("\n=== DAFTAR STOK BARANG LISHOP ===")
    with open(nama_file, "r", encoding="utf-8") as file:
        isi = file.read() #mengecek apakah file stok ada isi
        if not isi:
            print("Tidak ada barang stok!")
        else:
            print(f"| {"Kode Barang" : <12} | {"Nama Barang" : <12} | {"Stok" : >5} |")
            print("-" * 39)
            #menampilkan isi data stok barang
            for KodeBarang in sorted(stok_dict.keys()):
                NamaBarang = stok_dict[KodeBarang]["Nama Barang"]
                Stok = stok_dict[KodeBarang]["Stok Barang"]
                print(F"| {KodeBarang:<12} | {NamaBarang:<12} | {int(Stok):>5} |")
            print("-" *39)

#buka_data = baca_stok(nama_file)
#tampilkan_semua(buka_data) #menampilkan data

