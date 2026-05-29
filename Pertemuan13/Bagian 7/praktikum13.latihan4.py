#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 13 - Graph III: Spanning Trees (Kruskal’s & Prim’s Approaches)
#======================================

#Latihan 4: Studi Kasus

#======================================

#Daftar edge: (bobot, node1, node2)
edges = [
    (4, "GedungA", "GedungB"),
    (2, "GedungA", "GedungC"),
    (3, "GedungB", "GedungD"),
    (1, "GedungC", "GedungD"),
    (5, "GedungA", "GedungD")
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
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

# 1. Saya menggunakan algoritma kruskal karena menurut saya lebih cepat dan efisien untuk graph kecil/sedikit
# 2. Edge yang dipilih GedungC - GedungD, GedungA - GedungC, GedungB - GedungD
# 3. Total biaya bobot minimumnya adalah 6
# 4. MST cocok pada kasus ini karena tujuan kampus adalah menghubungkan semua gedung dengan biaya pemasangan kabel sekecil atau seminimal mungkin tanpa adanya jalur yang tidak diperlukan