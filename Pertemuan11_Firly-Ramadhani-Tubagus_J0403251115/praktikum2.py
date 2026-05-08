#==========================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#==========================
def createGraph(edges):
    adj={}
    #menambahkan edge ke adjacency listnya
    for it in edges:
        u=it[0]
        v=it[1]

        #kalau node belum ada
        if u not in adj:
            adj[u]=[]
        
        if v not in adj:
            adj[v]=[]

        #tambahkan edge    
        adj[u].append(v)
        #karena graphnya tidak berarah
        adj[v].append(u)
    return adj

if __name__=="__main__":
    #list edges nya
    edges = [["A","B"],["A","C"],["B","D"],["C","D"]]
    #membuat graph menggunakan edgesnya
    adj = createGraph(edges)
    #memanggil
    print("Adjacency List:")
    for node in adj:
        print(f"{node}:", end=" ")
        for j in adj[node]:
            print(j, end=" ")
        print()