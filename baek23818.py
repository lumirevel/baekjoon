from sys import stdin


class DisjointSet:
    class Item:
        def __init__(self):
            self.p = self
            self.rank = 0

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
counterList = []
for _ in range(N):
    itemList.append(DisjointSet.Item())
    counterList.append(DisjointSet.Item())
relationList = []
for _ in range(M):
    t, a, b = map(int, stdin.readline().split(" "))
    relationList.append((t, a-1, b-1))
queryList = []
for _ in range(K):
    a, b = map(int, stdin.readline().split(" "))
    queryList.append((a-1, b-1))


for t, a, b in relationList:
    itemA = itemList[a]
    itemB = itemList[b]
    counterA = counterList[a]
    counterB = counterList[b]
    if t == 0:
        DisjointSet.unionItem(itemA, itemB)
        DisjointSet.unionItem(counterA, counterB)
    elif t == 1:
        DisjointSet.unionItem(counterA, itemB)
        DisjointSet.unionItem(itemA, counterB)


for a, b in queryList:
    itemA = itemList[a]
    itemB = itemList[b]
    counterA = counterList[a]
    counterB = counterList[b]
    if DisjointSet.findSetItem(itemA) == DisjointSet.findSetItem(itemB) and DisjointSet.findSetItem(counterA) == DisjointSet.findSetItem(itemB):
        print("Error")
    elif DisjointSet.findSetItem(itemA) == DisjointSet.findSetItem(itemB):
        print("Friend")
    elif DisjointSet.findSetItem(counterA) == DisjointSet.findSetItem(itemB):
        print("Enemy")
    else:
        print("Unknown")
