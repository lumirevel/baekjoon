from sys import stdin
N = int(stdin.readline())

adjList = []
visited = []
for _ in range(N):
    adjList.append([])
    visited.append(False)
for _ in range(N-1):
    u, v = map(int, stdin.readline().rstrip().split(" "))
    adjList[u - 1].append(v - 1)

def bwMinColoredCount(adjList, node=0):
    visited[node] = True
    bMinColoredCount = 1
    wMinColoredCount = 0
    mustB = False
    for child in adjList[node]:
        if not visited[child]:
            b,w = bwMinColoredCount(adjList, child)
            bMinColoredCount += min(b,w)
            wMinColoredCount += b
    return bMinColoredCount, wMinColoredCount

bMinColoredCount, wMinColoredCount = bwMinColoredCount(adjList)
print(min(bMinColoredCount, wMinColoredCount))