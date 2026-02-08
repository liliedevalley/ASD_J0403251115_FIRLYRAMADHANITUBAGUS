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
