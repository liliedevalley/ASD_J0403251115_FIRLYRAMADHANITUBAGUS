#==========================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#==========================

#STUDI KASUS JARINGAN KOMPUTER

# ==========================
# DATA NODE DAN EDGE
# ==========================

# dictionary node dan keterangannya
nodes = {
    "A": "Router",
    "B": "Switch",
    "C": "Switch",
    "D": "PC1",
    "E": "Server",
    "F": "PC2"
}

# daftar edge / hubungan antar node
edges = [
    ["A", "B"],
    ["A", "C"],
    ["B", "C"],
    ["B", "D"],
    ["B", "E"],
    ["C", "E"],
    ["C", "F"]
]

# ==========================================
# ADJACENCY LIST
# ==========================================

def createAdjList(edges):
    adj = {}

    # menambahkan tiap edge ke adjacency list
    for edge in edges:
        u = edge[0]
        v = edge[1]

        # jika node belum ada
        if u not in adj:
            adj[u] = []

        if v not in adj:
            adj[v] = []

        # tambahkan edge
        adj[u].append(v)

        # karena graph tidak berarah
        adj[v].append(u)
    return adj


# ==========================================
# ADJACENCY MATRIX
# ==========================================

def createAdjMatrix(nodes, edges):
    node_list = list(nodes.keys())
    n = len(node_list)

    # membuat matrix berisi 0
    mat = [[0 for _ in range(n)] for _ in range(n)]

    # mapping node ke index
    index = {}
    for i in range(n):
        index[node_list[i]] = i

    # mengisi edge ke dlm matrix
    for edge in edges:
        u = edge[0]
        v = edge[1]

        i = index[u]
        j = index[v]

        mat[i][j] = 1
        mat[j][i] = 1   #karena graph tidak berarah
    return mat, node_list


# ==========================================
# PROGRAM UTAMA
# ==========================================

if __name__ == "__main__":
    # =========================
    # MEMBUAT ADJACENCY LIST
    # =========================

    adj = createAdjList(edges)
    print("=== ADJACENCY LIST ===")

    for node in adj:
        print(f"{node} ({nodes[node]}) :", end=" ")
        for neighbor in adj[node]:
            print(neighbor, end=" ")
        print()

    # =========================
    # MEMBUAT ADJACENCY MATRIX
    # =========================

    mat, node_list = createAdjMatrix(nodes, edges)
    print("\n=== ADJACENCY MATRIX ===")

    # kepala/header matrix
    print("   ", end=" ")
    for node in node_list:
        print(node, end=" ")
    print()

    # untuk isi matrix
    for i in range(len(mat)):
        print(node_list[i], end="  ")
        for j in range(len(mat[i])):
            print(mat[i][j], end=" ")
        print()

    # =========================
    # MENAMPILKAN NODE
    # =========================

    print("\n=== DAFTAR NODE ===")
    for kode, nama in nodes.items():
        print(kode, "=", nama)

    # =========================
    # MENAMPILKAN EDGE
    # =========================

    print("\n=== DAFTAR EDGE ===")
    for u, v in edges:
        print(
            u, f"({nodes[u]})",
            "<->",
            v, f"({nodes[v]})"
        )

    # =========================
    # JUMLAH NODE DAN EDGE
    # =========================

    print("\nJumlah Vertex :", len(nodes))
    print("Jumlah Edge   :", len(edges))