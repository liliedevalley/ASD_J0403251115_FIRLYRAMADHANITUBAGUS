#==========================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#==========================
def createGraph(edges):
    adj = {}
    #looping tiap baris matrix
    for i in range(len(edges)):

        #list kosong untuk node i
        adj[i] = []

        for j in range(len(edges[i])):

            if edges[i][j] == 1:
                adj[i].append(j)

    return adj

if __name__ == "__main__":

    matrix = [
        [0,1,1,0],
        [1,0,1,0],
        [1,1,0,1],
        [0,0,1,0]
    ]
    #membuat graphnya
    adj = createGraph(matrix)
    print("Adjacency List:")
    for node in adj:
        print(f"{node}:", end=" ")
        for j in adj[node]:
            print(j, end=" ")
        print()