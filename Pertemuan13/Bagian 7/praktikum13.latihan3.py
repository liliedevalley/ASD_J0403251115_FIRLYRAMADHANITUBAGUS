#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 13 - Graph III: Spanning Trees (Kruskal’s & Prim’s Approaches)
#======================================

#Latihan 3: Implementasi Algoritma Prims

#======================================

import heapq

graph = {
    "A" : {"B":4, "C":2, "D":5},
    "B" : {"A":4, "D":3},
    "C" : {"A":2, "D":1},
    "D" : {"A":5, "B":3, "C":1}
}

def prim(graph, start):
    visited = set([start])

    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0 

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, "A")

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total Bobot = ", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# 1. Node awal yang digunakan adalah A
# 2. Edge yang dipilih pertama kali adalah A - C
# 3. Prim menentukan edge dengan cara memilih sisi dengan bobot terkecil dari node yang sudah ada ke node yang belum dikunjungi
# 4. Total bobot MST yang dihasilkan adalah 6
# 5. Perbedaan Prim dan Kruskal adalah Prim membangun tree secara bertahap dari satu node ke node lain, sedangkan Kruskal membangunnya dengan cara memilih edge bobot terkecil (tidak ngurut tapi yang penting tidak menjadi siklus)