#PREGUNTA 3: Encuentra el camino entre los vértices dados en un gráfico dirigido


class Graph:
  def __init__(self,edges,n):
    self.adyacencyList = [[] for i in range(n)]
    
    for (src,dest) in edges:
      self.adyacencyList[src].append(dest)
      
  def findPath(self,src,dest):
    visited = [False] * len(self.adyacencyList)
    path = []
    self.findPathUtil(src,dest,visited,path)
    return 1 if len(path) else 0
  
  def findPathUtil(self,src,dest,visited,path):
    visited[src] = True
    path.append(src)
    if src == dest:
      return True
    for i in self.adyacencyList[src]:
      if not visited[i]:
        if self.findPathUtil(i,dest,visited,path):
          return True
    path.pop()
    return False
  
  
edges = [(0,3),(1,0),(1,2),(1,4),(2,7),(3,4),(3,5),(4,3),(4,6),(5,6),(6,7)]
G = Graph(edges,8)
src_node =  0
dest_node = 7

print(G.findPath(src_node,dest_node))



"""
  Salida del programa:
    1 (si existe un camino desde el nodo_inicial al nodo_final)
    0 (si no existe un camino desde el nodo_inicial al nodo_final
"""