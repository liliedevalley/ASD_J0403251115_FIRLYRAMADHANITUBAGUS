#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 12 - Graph II: Shortest Path
#======================================

#Latihan 1: Weighted Graph dan Perhitungan Jalur

#======================================

#Representasi weighted graph menggunakan dictionary bersarang

graph = {
    "A" : {"B" : 4, "C" : 2},
    "B" : {"D" : 5},
    "C" : {"D" : 1},
    "D" : {}
}

#Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph["A"]["B"] + graph["B"]["D"] #A -> B -> D
jalur_2 = graph["A"]["C"] + graph["C"]["D"] #A -> C -> D

print(f"Jalur 1: A -> B -> D = {jalur_1}")
print(f"Jalur 2: A -> C -> D = {jalur_2}")

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


#Pertanyaan Analisis
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit?

#Jawaban Analisis
# 1. Total bobot jalur A -> B -> D adalah 9
# 2. Total bobot jalur A -> C -> D adalah 3
# 3. Jalur yang dipilih sebagai jalur terpendek adalah jalur 2 atau A -> C -> D
# 4. Kenapa tidak selalu ditentukan dari jumlah edge karena meskipun jalur melalui
#lebih banyak edge, total biaya perjalanan bisa saja lebih kecil entah karena ada
#edge yang mempunyai bobot negatif atau karena total bobot jalur tersebut lebih sedikit
#daripada jalur yang mempunyai jumlah edge lebih sedikit