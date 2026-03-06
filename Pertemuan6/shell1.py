# ==========================================================
# Pertemuan 6
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Shell Sort Ascending
#===========================================================

def gapInsertionSort(data,start,gap):
    for i in range(start+gap, len(data), gap):
        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] > currentvalue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue


def shellsort(data):
    sublistcount = len(data)//2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", data)

        sublistcount = sublistcount//2


data = [54,26,93,17,77,31,44,55,20]
shellsort(data)
print(data)