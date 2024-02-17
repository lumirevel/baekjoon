from sys import setrecursionlimit, stdin
setrecursionlimit(200005)
n, k = map(int, stdin.readline().split(" "))
adjList = []
for _ in range(n):
    adjList.append([])
for _ in range(n-1):
    p, c = map(int, stdin.readline().split(" "))
    adjList[p].append(c)
func = [None] * n
for i, num in enumerate(map(int, stdin.readline().split(" "))):
    func[num] = i


depthList = [0] * n
visited = [False] * n
def DFS(now = 0, depth = 0):
    visited[now] = True
    depthList[now] = depth
    for child in adjList[now]:
        if not visited[child]:
            DFS(child, depth+1)

DFS()


print(depthList[func[k]])
