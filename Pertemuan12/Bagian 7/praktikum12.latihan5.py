#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 12 - Graph II: Shortest Path
#======================================

#Latihan 5: Studi Kasus dengan Program Shortest Path

#======================================

import heapq

#Graph lokasi antar kota
#Jarak dibuat dalam hitungan jam
graph = {
    "Bogor" : {"Jakarta" : 5, "Depok" : 2},
    "Depok" : {"Jakarta" : 2, "Bandung" : 6},
    "Jakarta" : {"Bandung" : 7},
    "Bandung" : {}
}

def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float("inf") for node in graph}

    #Jarak dari start ke start adalah 0
    distances[start] = 0

    #Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        #Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        #Maka proses dilewati
        if current_distance > distances[current_node]:
            continue 

        #Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            #Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, "Bogor")
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(kota, "=", jarak, "jam")


# Pertanyaan Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah node kota "Bogor"
# 2. Node yang memiliki jarak paling kecil dari node awal (selain node itu sendiri) adalah node kota "Depok"
# 3. Node yang memiliki jarak paling besar dari node awal adalah node kota "Bandung"
# 4. Algoritma Dijkstra pada kasus ini bekerja dengan cara membandingkan dua node yang kota yang bersebelahan dari node awal lalu memilih node dengan bobot terkecil, begitu seterusnya sampai menghasilkan jarak antar kota