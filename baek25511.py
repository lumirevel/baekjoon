from sys import setrecursionlimit, stdin
setrecursionlimit(100005)
n, k = map(int, stdin.readline().split(" "))
adjList = []
for _ in range(n):
    adjList.append([])
for _ in range(n-1):
    p, c = map(int, stdin.readline().split(" "))
    adjList[p].append(c)
numList = list(map(int, stdin.readline().split(" ")))


depthList = [0] * n
visited = [False] * n
def DFS(now = 0, depth = 0):
    visited[now] = True
    depthList[now] = depth
    for child in adjList[now]:
        if not visited[child]:
            DFS(child, depth+1)

def binarySearch(chart, item, start = 0, end = None):
    if end is None:
        end = len(chart)-1
    mid = (start+end) // 2
    if item < chart[mid]:
        return binarySearch(chart, item, start, mid-1)
    elif item > chart[mid]:
        return binarySearch(chart, item, mid+1, end)
    else:
        return mid

DFS()


print(depthList[binarySearch(numList, k)])
