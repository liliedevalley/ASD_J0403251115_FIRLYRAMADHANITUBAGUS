# ==========================================================
# Pertemuan 6
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Selection Sort Ascending
#===========================================================

def selectionsort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1, fillslot+1):
            if data[location]>data[positionOfMax]:
                positionOfMax = location
        
        #SWAP
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp

data=[54,26,93,17,77,31,44,55,20]
selectionsort(data)
print(data)