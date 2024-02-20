from sys import stdin


class DisjointSet:
    class Item:
        def __init__(self):
            self.p = self
            self.rank = 0
            self.counter = None

    @staticmethod
    def linkItem(x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    @staticmethod
    def unionItem(x, y):
        DisjointSet.linkItem(DisjointSet.findSetItem(x), DisjointSet.findSetItem(y))

    @staticmethod
    def findSetItem(x):
        if x != x.p:
            x.p = DisjointSet.findSetItem(x.p)
        return x.p


N, M, K = map(int, stdin.readline().split(" "))
itemList = []
for _ in range(N):
    itemList.append(DisjointSet.Item())
relationList = []
for _ in range(M):
    t, a, b = map(int, stdin.readline().split(" "))
    relationList.append((t, itemList[a-1], itemList[b-1]))
queryList = []
for _ in range(K):
    a, b = map(int, stdin.readline().split(" "))
    queryList.append((itemList[a-1], itemList[b-1]))


for t, itemA, itemB in relationList:
    setA = DisjointSet.findSetItem(itemA)
    setB = DisjointSet.findSetItem(itemB)
    if setA.counter is None:
        setA.counter = DisjointSet.Item()
    if setB.counter is None:
        setB.counter = DisjointSet.Item()
    if t == 0:
        DisjointSet.unionItem(setA, setB)
    elif t == 1:
        DisjointSet.unionItem(setA.counter, setB)
        DisjointSet.unionItem(setB.counter, setA)


for itemA, itemB in queryList:
    if itemA.counter is None or itemB.counter is None:
        print("Unknown")
    elif DisjointSet.findSetItem(itemA) == DisjointSet.findSetItem(itemB) and DisjointSet.findSetItem(itemA.counter) == DisjointSet.findSetItem(itemB):
        print("Error")
    elif DisjointSet.findSetItem(itemA) == DisjointSet.findSetItem(itemB):
        print("Friend")
    else:
        print("Enemy")
