# ==========================================================
# Pertemuan 6
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Latihan
#===========================================================


#Menggunakan BubbleSort
def shortBubblesort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    passnum = passnum-1
    return alist

datahasil = [43,76,12,89,33,57,98,22,68,9]
#print(datahasil)

#1. Top 5 kandidat yang paling tinggi
shortBubblesort(datahasil)
top5 = shortBubblesort(datahasil)
print(f"Top 5 : {top5[:5]}")

#2. Kandidat berapa saja yang lolos
data = []
for i in range(len(datahasil)):
    data.append((i+1, datahasil[i]))

print("\nKandidat yang lolos:")
for i in range(5):
    print("Kandidat", data[i][0], "dengan skor", data[i][1])