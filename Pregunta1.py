# PREGUNTA 1: Comprobar si un grafo está fuertemente conectado o no

class Graph:
  def __init__(self,edges,n):
    self.adyacencyList = [[] for i in range(n)]
    
    for (src,dest) in edges:
      self.adyacencyList[src].append(dest)
      
  def isStronglyConnected(self):
    for i in range(len(self.adyacencyList)):
      visited = [False] * len(self.adyacencyList)
      self.isStronglyConnectedUtil(i,visited)
    return 0 if False in visited else 1
  
  def isStronglyConnectedUtil(self,src,visited):
    visited[src] = True
    for i in self.adyacencyList[src]:
      if not visited[i]:
        self.isStronglyConnectedUtil(i,visited)
      
      
if __name__ == "__main__":

  edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
 
  # total de nodos en el grafo
  n = 5
  
  G = Graph(edges, n)
  
  print(G.isStronglyConnected())
"""  
  Salida del programa:
    1 (si es fuertemente conectado SCC)
    0 (si no lo es)
"""