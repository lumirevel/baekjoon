from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
N = int(stdin.readline())

adjList = []
visited = []
for _ in range(N):
    adjList.append([])
    visited.append(False)
for _ in range(N-1):
    u, v = map(int, stdin.readline().rstrip().split(" "))
    adjList[u - 1].append(v - 1)
    adjList[v - 1].append(u - 1)

def bwMinColoredCount(adjList, node=0):
    visited[node] = True
    bMin = 1
    wMin = 0
    for child in adjList[node]:
        if not visited[child]:
            b,w = bwMinColoredCount(adjList, child)
            bMin += min(b, w)
            wMin += b
    return bMin, wMin

bMinColoredCount, wMinColoredCount = bwMinColoredCount(adjList)
print(min(bMinColoredCount, wMinColoredCount))