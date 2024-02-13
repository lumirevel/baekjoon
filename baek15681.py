from sys import stdin, setrecursionlimit
setrecursionlimit(100005)
N, R, Q = map(int, stdin.readline().split(" "))
adjList = []
for _ in range(N):
    adjList.append([])
for _ in range(N-1):
    u, v = map(int, stdin.readline().split(" "))
    adjList[u-1].append(v-1)
    adjList[v-1].append(u-1)
queryList = []
for _ in range(Q):
    queryList.append(int(stdin.readline()))

countList = [1] * N
visited = [False] * N
def DFS(now):
    visited[now] = True
    for next in adjList[now]:
        if not visited[next]:
            DFS(next)
            countList[now] += countList[next]
DFS(R-1)
for query in queryList:
    print(countList[query-1])