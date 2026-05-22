#======================================
#Nama: Firly Ramadhani T
#NIM: J0403251115
#Kelas: A1
#Praktikum 12 - Graph II: Shortest Path
#======================================

#Materi 1

#======================================

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi berulang
    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():

                if distances[node] + weight < distances[neighbor]:
                    
                    distances[neighbor] = distances[node] + weight

    return distances
