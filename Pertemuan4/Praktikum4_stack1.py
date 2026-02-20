# ==========================================================
# Pertemuan 4
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Implementasi Dasar: Stack
#===========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diintimasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data apda list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)


#Stack ada operasi push (memasukkan head baru) dan pop (menghapus head lama)
#A -> B -> C -> None

class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def is_empty(self): #stack kosong jika top none
        return self.top is None

    def push(self, data): #memasukkan data baru
        #1> Membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2> Node baru harus menuju ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3> Geser top pindah ke node Baru
        self.top = nodeBaru

    def pop(self): #mengambil / menghapus node paling atas (head/top)
        
        if self.is_empty(): 
            print("Stack Kosong, tidak bisa pop!")
            return None
        
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        #B -> A -> None
        self.top = self.top.next  #geser top ke node berikutnya
        return data_terhapus
        #A -> None

    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        # Top -> A -> B
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next 
        print("None")

#Instantiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print(f"Peek (Lihat Top): {s.peek()}")
s.pop()
s.tampilkan()
print(f"Peek (Lihat Top): {s.peek()}")