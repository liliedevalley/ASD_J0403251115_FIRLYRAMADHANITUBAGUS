# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Firly Ramadhani Tubagus
# NIM     : J0403251115
# Kelas   : TPL A1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {} #inisialisasi data ke dictionary
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip() #strip untuk menghapus spasi diakhir
                kode, namabuku, harga = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
                database_buku[kode] = { #simpan ke dalam dictionary
                    "Nama Buku" : namabuku,
                    "Harga" : int(harga)
                }
    
    except FileNotFoundError: #kalau misalkan filenya tidak ada
        print("File tidak ditemukan!")
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul #menyimpan judul buku
        self.next = None #pointer untuk ke node selanjutnya

class LinkedListPromosi:
    def __init__(self):
         self.head = None #node pertamanya

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        nodebaru = Node(judul)

        if self.head is None: #kalau linked listnya masih kosong
            self.head = nodebaru #node barunya menjadi head
        else:
            current = self.head #kalau gk kosong cari node terakhir
            while current.next:
                current = current.next
            current.next = nodebaru #menambahkan node baru di akhir list

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        current = self.head #mulai dari head/ node pertama

        if current is None: #kalau listnya masih kosong
            print("Belum ada buku dalam daftar promosi")
            return
        print("Daftar buku promosi:")
        while current: #traversal linked list, menelusuri node
            print("-", current.judul)
            current = current.next

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = [] #list sebagai struktur queue

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        self.antrean.append(nama_pelanggan) #pelanggan dimasukkan ke belakang antrian
        print(nama_pelanggan, "masuk ke dalam antrean.")

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if len(self.antrean) ==0: #kalau antreannya kosong
            print("Tidak ada pelanggan.")
        else:
            pelanggan = self.antrean.pop(0) #menghapus pelanggan pertama yang daatang
            print(f"Sedang melayani: {pelanggan}")

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    for i in range(1, len(list_harga)):
        key = list_harga[i] #menyimpan nilai yang akan disisipkan
        j = i - 1 #membandingkan dengan elemen sebelumnya

        while j >= 0 and list_harga[j] > key: #menggeser elemen, elemen lebih besar ke sebelah kanan
            list_harga[j+1] = list_harga[j]
            j = j - 1

        list_harga[j+1] = key #menempatkan ulang key
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            #print("\nKatalog Buku:", data_buku)
            print("Katalog Buku:\n")
            for kode, info in data_buku.items():
                print(kode, "-", info["Nama Buku"], "-", info["Harga"])
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            print("1. Tambah Antrean")
            print("2. Layani Pelanggan")
            pilih = input("Pilih: ")
            
            if pilih=="1":
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif pilih=="2":
                antrean_toko.layani_pelanggan()
            
        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()