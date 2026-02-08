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
            print(f"| {"Kode Barang" : <12} | {"Nama Barang" : <15} | {"Stok" : >5} |")
            print("-" * 42)
            #menampilkan isi data stok barang
            for KodeBarang in sorted(stock_dict.keys()):
                NamaBarang = stock_dict[KodeBarang]["Nama Barang"]
                Stok = stock_dict[KodeBarang]["Stok Barang"]
                print(F"| {KodeBarang:<12} | {NamaBarang:<15} | {int(Stok):>5} |")
            print("-" *42)

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
def tambah_barang(stock_dict):
    """Menambah barang baru ke dalam stock_dict"""
    print("===Menambah Barang Baru===")

    while True: #mengecek apakah kode barang sudah ada atau belum
        kode = input("Masukkan kode barang baru: ").strip()
        if kode in stock_dict:
            print("Maaf kode barang sudah dipakai! Silahkan gunakan kode lain")
        else:
            break #perulangan berhenti jika kode barang belum dipakai

    nama = input("Masukkan nama barang: ").strip()
    stok_awal = int(input("Masukkan jumlah stok awal: "))
    stock_dict[kode]= { #menambahkan barang baru ke dalam dict
        "Nama Barang" : nama,
        "Stok Barang" : int(stok_awal)
    }
    print("Barang berhasil ditambahkan!")

#tambah_barang(buka_data)

#------------------
#fungsi 5: update stok barang
#------------------
def update_stok(stock_dict):
    """Mengubah stok barang (menambah atau mengurangi) namun stok tidak boleh menjadi negatif"""
    #mencari kode barang yang ingin diubah
    kode = input("Masukkan kode barang yang ingin di update: ").strip()
    if kode not in stock_dict:
        print("Kode barang tidak ditemukan! Harap masukkan kode yang benar")
        return
    
    Nama = stock_dict[kode]["Nama Barang"] 
    Stok = stock_dict[kode]["Stok Barang"]
    print("===Data Barang Sebelumnya===") #menampilkan data lama barang
    print(F"Kode Barang: {kode}")
    print(F"Nama Barang: {Nama}")
    print(f"Stok Barang: {Stok}")

    print("-" * 10)
    print("Pilih jenis update:")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")

    pilihan = input("Masukkan pilihan(1/2): ").strip()
    if pilihan not in ("1", "2"): #jika user memilih diluar 1 dan 2
        print("Pilihan tidak tersedia!")
        return

    try:
        jumlah = int(input("Masukkan jumlah untuk mengubah: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
    if pilihan =="1":
        stokbaru = Stok + jumlah
    else:
        stokbaru = Stok - jumlah

    if stokbaru < 0:
        print("Stok tidak boleh bernilai negatif!")
        return
    
    stock_dict[kode]["Stok Barang"] = stokbaru
    print("Stok berhasil diperbarui!")
    print("===Data Barang Setelah di Update===") #menampilkan stok yang telah diperbaru
    print(F"Kode Barang: {kode}")
    print(F"Nama Barang: {Nama}")
    print(f"Stok Barang: {stokbaru}")

#update_stok(buka_data)

#------------------
#fungsi 6: menyimpan data
#------------------
def simpan_stok(nama_file, stock_dict):
    """Berfungsi untuk menyimpan setiap perubahan"""
    with open(nama_file, "w", encoding="utf-8") as file:
        for KodeBarang in sorted(stock_dict.keys()):
            NamaBarang = stock_dict[KodeBarang]["Nama Barang"]
            Stok = stock_dict[KodeBarang]["Stok Barang"]
            file.write(f"{KodeBarang}, {NamaBarang}, {Stok}\n")

#------------------
#Program Utama
#------------------
def main():
    #membaca data dari file saat program dimulai
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK BARANG LISHOP===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        print("\nJangan lupa untuk selalu menyimpan setiap perubahan!")

        pilihan = input("Pilih menu: ").strip()
        if pilihan=="1":
            tampilkan_semua(stok_barang)
        elif pilihan=="2":
            cari_barang(stok_barang)
        elif pilihan=="3":
            tambah_barang(stok_barang)
        elif pilihan=="4":
            update_stok(stok_barang)
        elif pilihan=="5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan!")
        elif pilihan=="0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid! Silahkan coba lagi!")

if __name__ == "__main__" :
    main()