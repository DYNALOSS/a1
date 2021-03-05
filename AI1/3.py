from _collections import defaultdict
class Graph:

    def __init__(self,vertices):
        self.ver = vertices
        self.graph=defaultdict(list)
    
    def edgeadd(self,u,v):
        self.graph[u].append(v)

    def print(self):
        print(self.graph)
    
    def DLS(self,src,tar,maxD):
        if src==tar:
            return True
        if maxD<=0 : return False
        for i in self.graph[src]:
            if(self.DLS(i,tar,maxD-1)): return True
        return False

g=Graph(9)
g.edgeadd(0,1)
g.edgeadd(0,2)
g.edgeadd(1,3)
g.edgeadd(1,4)
g.edgeadd(2,5)
g.edgeadd(2,6)
g.edgeadd(3,7)
g.edgeadd(3,8)

tar=8
maxD=2
src=0

if g.DLS(src,tar,maxD)==True:
    print("target %d is reachable from soruce %d within maxDepth %d" % (tar, src,maxD))
else :
    print("target %d is not reachable from soruce %d within maxDepth %d" % (tar, src,maxD))