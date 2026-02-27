# ==========================================================
# Pertemuan 5
#
# Nama : Firly Ramadhani Tubagus
# NIM : J0403251115
# Kelas : A1
# ==========================================================

#===========================================================
# Latihan 1: Rekursi Pangkat
#===========================================================

def pangkat(a,n):
#a berperan sebagai bilangan basis
#n berperan sebagai bilangan pangkat

    #Base Case
    if n==0: #jika pangkat 0 maka kembalikan nilai 1
        return 1
    
    #Recursive Case
    return a * pangkat(a, n-1)

print(pangkat(2,4))
#Alur program
#pangkat(2,4) = 2 * pangkat(2,3)
#pangkat(2,3) = 2 * pangkat(2,2)
#pangkat(2,2) = 2 * pangkat(2,1)
#pangkat(2,1) = 2 * pangkat(2,0)
#pangkat(2,0) = 2 * 1

#print(pangkat(3)) #Error, karena n tidak punya nilai default