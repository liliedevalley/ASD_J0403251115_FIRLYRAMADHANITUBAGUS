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
def tampilkan_semua(stock_dict):
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
            for KodeBarang in sorted(stock_dict.keys()):
                NamaBarang = stock_dict[KodeBarang]["Nama Barang"]
                Stok = stock_dict[KodeBarang]["Stok Barang"]
                print(F"| {KodeBarang:<12} | {NamaBarang:<12} | {int(Stok):>5} |")
            print("-" *39)

buka_data = baca_stok(nama_file)
#tampilkan_semua(buka_data) #menampilkan data

#------------------
#fungsi 3: mencari stok barang berdasarkan kode barang
#------------------
def cari_barang(stock_dict):
    """Mencari barang berdasarkan kode barang"""
    #membuat input kode barang yang ingin dicari
    kode_cari = input("Masukkan kode barang yang ingin anda cari: ").strip()

    if kode_cari in stock_dict: #mengecek apakah kode ada di dalam data barang
        Nama = stock_dict[kode_cari]["Nama Barang"]
        Stok = stock_dict[kode_cari]["Stok Barang"]
        print("===Data Barang Ditemukan!===")
        print(F"Kode Barang: {kode_cari}")
        print(F"Nama Barang: {Nama}")
        print(f"Stok Barang: {Stok}")
    else:
        print("Barang yang anda cari tidak ditemukan! Pastikan kode barang benar!")

#cari_barang(buka_data)

#------------------
#fungsi 4: menambah barang baru
#------------------
def tambah_barang(stok_dict):
    """Menambah barang baru ke dalam stock_dict"""
    print("===Menambah Barang Baru===")

    while True:
        kode = input("Masukkan kode barang baru: ").strip()
        if kode in stok_dict:
            print("Maaf kode barang sudah dipakai! Silahkan gunakan kode lain")
        else:
            break

    nama = input("Masukkan nama barang: ").strip()
    stok_awal = int(input("Masukkan jumlah stok awal: "))
    stok_dict[kode]= {
        "Nama Barang" : nama,
        "Stok Barang" : int(stok_awal)
    }
    print("Barang berhasil ditambahkan!")


#tambah_barang(buka_data)
