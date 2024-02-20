from sys import stdin
from queue import PriorityQueue
N, M = map(int, stdin.readline().split(" "))
totalCost = 0
adjList = []
for _ in range(N):
    adjList.append([])
for _ in range(M):
    a, b, c = map(int, stdin.readline().split(" "))
    adjList[a-1].append((c, b-1))
    adjList[b-1].append((c, a-1))
    totalCost += c


visited = [False] * N
def prim(now = 0):
    waiting = PriorityQueue()
    waiting.put((0, now))
    edgeCount = 0
    totalW = 0
    while waiting.queue:
        w, now = waiting.get()
        if not visited[now]:
            visited[now] = True
            edgeCount += 1
            totalW += w
            for w, v in adjList[now]:
                waiting.put((w, v))
    if edgeCount == N:
        return totalW
    return -1
saleW = prim()


if saleW != -1:
    print(totalCost-saleW)
else:
    print(-1)
