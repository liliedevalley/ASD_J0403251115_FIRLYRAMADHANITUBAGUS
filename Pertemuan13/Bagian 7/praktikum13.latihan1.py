#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 13 - Graph III: Spanning Trees (Kruskal’s & Prim’s Approaches)
#======================================

#Latihan 1

#======================================

#Daftar edge graph
edges = [
    ("A", "B"),
    ("A", "C"),
    ("A", "D"),
    ("C", "D"),
    ("B", "D")
]

#Spanning tree
spanning_tree = [
    ("A", "C"),
    ("C", "D"),
    ("D", "B")
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree = ", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# 1. Graph awal merupakan struktur umum yang mencakup seluruh titik(vertex/node) dan edge dan bisa memiliki siklus sedangkan spanning tree adalah bentuk khusus dari graph yang hanya memiliki vertex tanpa siklus/loop dengan menggunakan bobot seminimal mungkin
# 2. Karena spanning tree bertujuan untuk menghubungkan semua vertex dengan jalur paling sederhana/bobot paling sedikit
# 3. Karena spanning tree hanya menyimpan edge yang diperlukan tidak semuanya, spanning tree punya rumus n - 1 edge untuk n simpul