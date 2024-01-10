V, E = map(int, input().split(" "))

class SetElement:
    def __init__(self, v):
        self.v = v
        self.p = None
        self.rank = None

def makeSet(x):
    x.p = x
    x.rank = 0

def union(x,y):
    link(findSet(x),findSet(y))

def link(x,y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def findSet(x):
    if x != x.p:
        x.p = findSet(x.p)
    return  x.p

sets = []
edges = []
for v in range(V):
    element = SetElement(v)
    makeSet(element)
    sets.append(element)
for _ in range(E):
    A,B,C = map(int, input().split(" "))
    edges.append((sets[A-1],sets[B-1],C))
edges.sort(key=lambda x:x[2])

totalCost = 0
for edge in edges:
    u,v,w = edge
    if findSet(u) != findSet(v):
        union(u, v)
        totalCost += w

print(totalCost)
