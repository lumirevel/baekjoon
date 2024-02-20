from sys import stdin
n, m = map(int, stdin.readline().split(" "))
playList = []
for _ in range(m):
    playList.append(tuple(map(int, stdin.readline().split(" "))))


class DisjointSet:
    def __init__(self, size):
        self.itemList = []
        for i in range(size):
            self.itemList.append(DisjointSet.Item())

    class Item:
        def __init__(self):
            self.p = self
            self.rank = 0

    def union(self, x, y):
        self.linkItem(self.findSet(x), self.findSet(y))

    def linkItem(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank = y.rank + 1

    def findSet(self, x):
        return self.findSetItem(self.itemList[x])
    def findSetItem(self, x):
        if x != x.p:
            x.p = self.findSetItem(x.p)
        return x.p

connect = DisjointSet(n)
finish = 0
for i, play in enumerate(playList):
    u, v = play
    if connect.findSet(u) == connect.findSet(v):
        finish = i+1
        break
    else:
        connect.union(u, v)


print(finish)
