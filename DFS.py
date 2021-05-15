from collections import defaultdict
class Graph:
    def __init__(self):        
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def util(self,u, vis):
        vis[u]=True
        print u,
        for i in self.graph[u]:
            if vis[i]==False:
                self.util(i, vis)
    def DFS(self,v):
        n=len(self.graph)
        vis=[False]*n
        self.util(v,vis)
        '''for i in range(n):
            if vis[i]==False:
                self.util(i, vis)'''
        
g=Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print g.DFS(2)
