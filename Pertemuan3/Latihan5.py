# ===========================
# Nama: Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : TPL A1
# LATIHAN GANJIL
# ===========================

# ---------------------------
# LATIHAN 5: REVERSE SINGLY LINKED LIST
# ---------------------------

class Node:
    def __init__(self, data):
        self.data = data #mengisi node
        self.next = None #pointer ke node berikutnya

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def insert_at_end(self, data): #insert di akhir
        new_node = Node(data) #bikin node baru
        if not self.head: #kalau si linked listnya masih kosong jalanin ini
            self.head = new_node #node baru jadi head dan jadi tail
            self.tail = new_node
        else: #kalau udah ada linked list sebelumnya
            self.tail.next = new_node #nyambung tail lama ke node baru
            self.tail = new_node #pindahin tailnya ke node baru

    def reverse(self):
        prev = None #node sebelumnya tidak ada
        current = self.head #node yang akan diproses = node awal

        while current: #ketika si node terkini diproses
            next_node = current.next #node setelah node terkini disimpan menjadi node setelahnya
            current.next = prev #node sebelumnya dimasukkan/dipindahkan ke node setelah node terkini
            prev = current #node terkini menjadi node sebelumnya
            current = next_node #node setelahnya menjadi node terkini
        self.head = prev

    def display(self): #menampilkan
        temp = self.head
        while temp: 
            print(temp.data, end=" -> ")
            temp=temp.next
        print("null")

ll = LinkedList()

print("\nTampilan #1 sebelum dibalik: ")
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.display()
print("\nTampilan #1 Setelah dibalik: ")
ll.reverse()
ll.display()

print("\nTampilan #1 sebelum dibalik: ")
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.display()
print("\nTampilan #1 Setelah dibalik: ")
ll.reverse()
ll.display()