from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def util(self,u, vis, par):
        vis[u]=True
        for i in self.graph[u]:
            if not vis[i]:
                if self.util(i, vis, u): return True
            elif i!=par: return True
        return False
    def isCycle(self):
        vis=[False]*(self.v)
        for i in range(self.v):
            if not vis[i]:
                if self.util(i,vis,-1): return True
        return False
g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.isCycle(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")

    
