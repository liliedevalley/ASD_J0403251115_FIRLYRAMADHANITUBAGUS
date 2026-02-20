# ==========================================================
# Pertemuan 4
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Implementasi Dasar: Node pada Linked List
#===========================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diintimasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data apda list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1>cara membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2>mendefinisikan head menghubungkan node : A-> B-> C-> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3>Traversal: menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#===========================================================
# Implementasi Dasar: Stack
#===========================================================

