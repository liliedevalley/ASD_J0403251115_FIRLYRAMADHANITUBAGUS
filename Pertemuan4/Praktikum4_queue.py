# ==========================================================
# Pertemuan 4
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Implementasi Dasar: Queue
#===========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diintimasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data apda list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class queue:
    #buat konstruktor untuk inisialisasi variabel front (depan) dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang

    def is_empty(self):
        return self.front is None

    #Membuat fungsi untuk menambahkan data baru
    def enqueue(self, data):
        nodeBaru = Node(data)

        #jika queue kosong, front dan rear merunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #jika queue tidak kosong, maka langsung letakkan data baru setelah rear, dan jalankan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear

    #menghapus data dari depan / front
    def dequeue(self, data):
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next #

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front -> ", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print(" Rear")

#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue("A")
q.tampilkan()