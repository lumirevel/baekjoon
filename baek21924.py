from sys import stdin
N, M = map(int, stdin.readline().split(" "))
totalCost = 0
edgeList = []
for _ in range(M):
    a, b, c = map(int, stdin.readline().split(" "))
    edgeList.append((c, a-1, b-1))
    totalCost += c


class DisjointSet:
    class Item:
        def __init__(self):
            self.p = self
            self.rank = 0

    def __init__(self, size):
        self.size = size
        self.elementList = []
        for _ in range(size):
            self.elementList.append(DisjointSet.Item())

    def linkItem(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank = y.rank + 1

    def union(self, x, y):
        self.linkItem(self.findSet(x), self.findSet(y))

    def findSet(self, x):
        return self.findSetItem(self.elementList[x])
    def findSetItem(self, x):
        if x.p != x:
            x.p = self.findSetItem(x.p)
        return x.p

edgeList.sort()
edgeCount = 0
saleW = 0
check = DisjointSet(N)
for w, u, v in edgeList:
    if check.findSet(u) != check.findSet(v):
        edgeCount += 1
        saleW += w
        check.union(u, v)


if edgeCount == N-1:
    print(totalCost-saleW)
else:
    print(-1)
