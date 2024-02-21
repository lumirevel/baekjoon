from sys import stdin
N, M, K = map(int, stdin.readline().split(" "))
relationList = []
for _ in range(M):
    t, a, b = map(int, stdin.readline().split(" "))
    relationList.append((t, a-1, b-1))
queryList = []
for _ in range(K):
    a, b = map(int, stdin.readline().split(" "))
    queryList.append((a-1, b-1))


class Item:
    def __init__(self):
        self.p = self
        self.rank = 0

def linkItem(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def unionItem(x, y):
    linkItem(findSetItem(x), findSetItem(y))

def findSetItem(x):
    if x != x.p:
        x.p = findSetItem(x.p)
    return x.p

itemList = []
counterList = []
for _ in range(N):
    itemList.append(Item())
    counterList.append(Item())
for t, a, b in relationList:
    itemA = itemList[a]
    itemB = itemList[b]
    counterA = counterList[a]
    counterB = counterList[b]
    if t == 0:
        unionItem(itemA, itemB)
        unionItem(counterA, counterB)
    elif t == 1:
        unionItem(counterA, itemB)
        unionItem(itemA, counterB)


for a, b in queryList:
    itemA = itemList[a]
    itemB = itemList[b]
    counterA = counterList[a]
    counterB = counterList[b]
    if findSetItem(itemA) == findSetItem(itemB) and findSetItem(counterA) == findSetItem(itemB):
        print("Error")
    elif findSetItem(itemA) == findSetItem(itemB):
        print("Friend")
    elif findSetItem(counterA) == findSetItem(itemB):
        print("Enemy")
    else:
        print("Unknown")
