#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 12 - Graph II: Shortest Path
#======================================

#Latihan 3: Implementasi Bellman-Ford

#======================================

#Weighted graph dengan bobot negatif
graph = {
    "A" : {"B" : 5, "C" : 4},
    "B" : {},
    "C" : {"B": -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    #Semua jarak awal dibuat tak hingga
    distances = {node: float("inf") for node in graph}

    #Jarak dari start ke start adalah 0
    distances[start] = 0

    #Bellman-Ford melakukan relaksasi sebanyak jumlah node -1
    for _ in range(len(graph)- 1):
        #Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                #Jika jarak ke node saat ini sudah diketahui
                #dan ditemukan ajrak yang lebih kecik ke neighbor,
                #maka lakukan update jarak
                if distances[node] != float("inf") and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, "A")

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


#Pertanyaan Analisis
#1. Berapa bobot langsung dari A ke B?
#2. Berapa total bobot jalur A -> C -> B?
#3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#5. Apa yang dimaksud dengan proses relaksasi edge?
#6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

#Jawaban Analisis
#1. Total bobot langsung dari A ke B adalah 5
#2. Total bobot jalur A -> C -> B adalah 2
#3. Jalur yang menghasilkan jarak lebih kecil menuju B adalah jalur A -> C -> B
#4. Karena algoritma Bellman-Ford mampu menangani graph dengan bobot negatif dan tetap menemukan jalur terpendek secara benar, dengan cara mengecek terlebih dahulu seluruh jalur sehingga bisa menemukan jalur dengan jarak terpendek walaupun ada node dengan bobot negatif
#5.Relaksasi edge merupakan proses untuk mengecek kembali apakah ada jalur yang lebih pendek kemudian mengupdate jaraknya kembali
#6. Perbendaan utama Bellman-Ford dan Dijkstra adalah cara mereka untuk memproses jalur, Bellman-Ford dapat menangani node yang memiliki bobot positif dan negatif sedangkan Dijkstra hanya mampu menangani node yang memiliki bobot positif.