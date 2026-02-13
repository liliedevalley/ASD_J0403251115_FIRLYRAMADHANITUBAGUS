# ===========================
# Nama: Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : TPL A1
# LATIHAN GANJIL
# ===========================

# ---------------------------
# LATIHAN 1 : MENGHAPUS NODE
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

    def delete_node(self,key):
        temp=self.head #mulainya dari node pertama
        if temp and temp.data ==key: #kalau node yang dihapusnya head
            self.head = temp.next #diganti headnya jadi ke node selanjutnya
            temp = None 
            return
        prev = None #save node sebelumnya
        while temp and temp.data != key: #mencari node yang memiliki nilai key
            prev = temp #disimpen ke node sebelumnya
            temp = temp.next 
        if temp is None: #kalau node yang dicari ga ketemu, return
            return
        prev.next = temp.next
        temp = None

    def display(self): #menampilkan
        temp = self.head
        while temp: 
            print(temp.data, end=" -> ")
            temp=temp.next
        print("null")

ll = LinkedList()

#Memasukkan nilai linked list
print("\nNilai Linked List sebelum dihapus:")
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(9)
ll.display()

print("\nNilai linked list setelah dihapus: ")
ll.delete_node(5)
ll.display()
