from collections import defaultdict
class Graph:
    def __init__(self):        
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,v):
        n=len(self.graph)
        vis=[False]*n
        s =[]
        s.append(v)
        while s:
            x =s.pop(0)
            vis[x]=True
            print x,
            for i in self.graph[x]:
                if vis[i]==False:
                    s.append(i)
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
print g.BFS(2)
