#PREGUNTA 2: Encontrar el vértice raíz de un grafo

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)

def DFS(graph, v, visited):
    visited[v] = True
    for u in graph.adjList[v]:
        if not visited[u]:
            DFS(graph, u, visited)

def findRootVertex(graph, n):
    for i in range(n):
      visited = [False] * n
      if not visited[i]:
        DFS(graph, i, visited)
      if False in visited:
        continue
      return i
    return -1


if __name__ == "__main__":

    edges =  [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]

    n = 6

    graph = Graph(edges, n)

    verticeRaiz = findRootVertex(graph, n)

    print(verticeRaiz)
 
"""
    Salida del programa:
      4 
      (-1 si no encuentra un nodo raíz).
"""   
