#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 13 - Graph III: Spanning Trees (Kruskal’s & Prim’s Approaches)
#======================================

#Latihan 2: Implementasi Sederhana Algoritma Kruskal

#======================================

#Daftar edge: (bobot, node1, node2)
edges = [
    (1, "C", "D"),
    (2, "A", "C"),
    (3, "B", "D"),
    (4, "A", "B"),
    (5, "A", "D")
]

#Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:
    #Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

# 1. Edge yang dipilih pertama kali adalah edge C - D karena bobotnya paling kecil
# 2. Karena algoritma Kruskal menerapkan pendekatan greedy untuk MST yang bertujuan untuk menghubungkan seluruh vertex dengan total edge sekecil mungkin
# 3. Total bobot MST yang dihasilkan kasus ini adalah 6
# 4. Edge tertentu tidak dipilih karena edge tidak boleh membentuk siklus/loop juga karena vertex sudah connected semua