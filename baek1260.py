# 내 version
# from sys import stdin, setrecursionlimit
# from collections import deque
# setrecursionlimit(100000)
# N, M, V = map(int, stdin.readline().rstrip().split(" "))
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     i, j = map(int, stdin.readline().rstrip().split(" "))
#     graph[i].append(j)
#     graph[j].append(i)
#
# dfsvisited = [False for _ in range(N+1)]
# def dfs(i):
#     dfsvisited[i] = True
#     print(i, end=" ")
#     for node in sorted(graph[i]):
#         if not dfsvisited[node]:
#             dfs(node)
#
# bfsvisited = [False for _ in range(N+1)]
# bfswillvisited = [False for _ in range(N+1)]
# def bfs(i):
#     willvisit = deque()
#     willvisit.append(i)
#     while willvisit:
#         now = willvisit.popleft()
#         bfsvisited[now] = True
#         print(now, end=" ")
#         for node in sorted(graph[now]):
#             if not bfsvisited[node]:
#                 if not bfswillvisited[node]:
#                     willvisit.append(node)
#                     bfswillvisited[node] = True
#
# dfs(V)
# print()
# bfs(V)

# 성범 version
from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(100000)
N, M, V = map(int, stdin.readline().rstrip().split(" "))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, stdin.readline().rstrip().split(" "))
    graph[i].append(j)
    graph[j].append(i)

dfsvisited = [False for _ in range(N+1)]
def dfs(i):
    dfsvisited[i] = True
    print(i, end=" ")
    for node in sorted(graph[i]):
        if not dfsvisited[node]:
            dfs(node)

isinqueue = [False for _ in range(N+1)]
def bfs(i):
    willvisit = deque()
    willvisit.append(i)
    isinqueue[i] = True

    while willvisit:
        now = willvisit.popleft()
        print(now, end=" ")
        for node in sorted(graph[now]):
            if not isinqueue[node]:
                willvisit.append(node)
                isinqueue[now] = True

dfs(V)
print()
bfs(V)