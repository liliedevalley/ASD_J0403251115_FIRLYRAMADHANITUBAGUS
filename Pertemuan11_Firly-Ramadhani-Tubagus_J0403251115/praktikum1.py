#==========================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#==========================
def createGraph(V,edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    #Menambahkan setiap edge ke adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        #karena graphnya tidak memiliki arah jadi setiap bertemu dijadikan 1
        mat[v][u]=1
    return mat

if __name__=="__main__":
    V = 4

    #list edgesnya
    edges = [[0,1],[0,2],[1,2],[2,3]]

    #membuat graphnya menggunakan edges
    mat = createGraph(V,edges)

    #memanggil
    print("Adjacency Matrix:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j],end=" ")
        print()