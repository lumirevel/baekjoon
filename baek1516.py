from sys import stdin
N = int(stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    L = list(map(int, stdin.readline().split()))
    graph[i] = [L[0], L[1: -1]]

visited = [False for _ in range(N+1)]
def DFS(i):
    visited[i] = True
    L = []
    for node in graph[i][1]:
        if not visited[node]:
            DFS(node)
        L.append(graph[node][2])
    if L:
        graph[i].append(max(L)+graph[i][0])
    else:
        graph[i].append(graph[i][0])

for i in range(1, N+1):
    DFS(i)

for i in range(1, N+1):
    print(graph[i][2])

# 성범이 같은 경우에는 그래프의 차수를 이용해서 풀었다고 한다.