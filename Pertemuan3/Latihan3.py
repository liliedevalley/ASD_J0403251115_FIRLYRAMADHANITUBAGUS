# ===========================
# Nama: Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : TPL A1
# LATIHAN GANJIL
# ===========================

# ---------------------------
# LATIHAN 3: MENCARI NODE PADA DOUBLE LINKED LIST
# ---------------------------

class Node:
    def __init__(self, data):
        self.data = data #mengisi node
        self.next = None #pointer ke node berikutnya
        self.prev = None  #pointer ke node sebelumnya

class doublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: #kalau double ll nya masih kosong
            self.head = new_node #node baru dijadiin head
            self.tail = new_node #node bru dijadiin tail
        else: #kalau udah ada isinya
            self.tail.next = new_node #tail lama disambung ke node bru
            new_node.prev = self.tail #previous new node baru disambungin ke tail lama
            self.tail = new_node #node baru dijadiin tail baru

    def search_dll(self, key):
        temp = self.head #mulai dari node pertama
        while temp:
            if temp.data == key: #kalau node yang dicari ketemu
                print(F"Elemen {key} ditemukan!")
                return
            temp = temp.next #kalau tidak ditemukan
        print(f"Elemen {key} tidak ditemukan!")

    def display_forward(self): #ditampilkan berurutan ke depan
        print("Traversing Forward: ")
        temp = self.head #node pertama
        while temp: #dimulai dari node pertama sampai ke node terakhir
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null") # kalau udah selesai print null
    
    def display_backward(self):
        print("Traversing backward: ")
        temp = self.tail #node terakhir
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

dll = doublyLinkedList()

print("\nIsi konten doubly linked list secara forward: ")
dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)
dll.display_forward()
print("\nIsi konten doubly linked list secara backward: ")
dll.display_backward()
print("\nMencari isi konten berupa angka 9: ")
dll.search_dll(9)
print("\nMencari isi konten berupa angka 10: ")
dll.search_dll(10)