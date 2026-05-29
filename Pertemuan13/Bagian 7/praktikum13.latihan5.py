#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 13 - Graph III: Spanning Trees (Kruskal’s & Prim’s Approaches)
#======================================

#Latihan 5: Tugas Mandiri

#======================================

#Daftar edge: (bobot, node1, node2)
edges = [
    (5, "Bogor", "Jakarta"),
    (2, "Bogor", "Depok"),
    (3, "Depok", "Jakarta"),
    (6, "Jakarta", "Bandung"),
    (4, "Depok", "Bandung")
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
# 1. Kasus apa yang dipilih?
# 2. Algoritma apa yang digunakan?
# 3. Edge mana saja yang dipilih dalam MST?
# 4. Berapa total bobot MST?
# 5. Mengapa edge tertentu tidak dipilih?

# 1. Kasus yang dipilih adalah kasus pertama yaitu Jaringan Jalan Antar Kota
# 2. Algoritma yang digunakan adalah algoritma kruskal karena lebih cepat dan efisien untuk graph kecil
# 3. Edge yang dipilih dalam MST adalah Bogor - Depok, Depok - Jakarta, Depok - Bandung
# 4. Total bobot MST sejumlah 9
# 5. Edge tertentu tidak dipilih karena jika dipilih semua dapat terjadi siklus, dan nilai bobotnya lebih besar daripada bobot edge yang dipilih, tujuan dari kasus ini sendiri adalah untuk mencari jalan dengan bobot seminimal mungkin sehingga bobot yang lebih besar tidak dipilih.