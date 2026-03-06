# ==========================================================
# Pertemuan 6
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Bubble Sort Ascending
#===========================================================


def bubblesort_asc(data): #Ascending
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                #Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp 

data = [54,26,93,17,77,31,44,55,20]
bubblesort_asc(data)
print(data)

#Latihan
def shortBubblesort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    passnum = passnum-1

alist = [20,30,40,90,50,60,70,80,100,110]

shortBubblesort(alist)
print(alist)
