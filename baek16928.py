# from sys import stdin
# from collections import deque
# K = 100
# graph = [[] for i in range(K+1)]
# for i in range(1, K+1):
#     for dice in range(1, 6+1):
#         if i < K-dice+1:
#             graph[i].append(i+dice)
# N, M = map(int, stdin.readline().rstrip().split(" "))
# for _ in range(N):
#     x, y = map(int, stdin.readline().rstrip().split(" "))
#     graph[x] = [y]
# for _ in range(M):
#     u, v = map(int, stdin.readline().rstrip().split(" "))
#     graph[u] = [v]
#
# isinqueue = [False for _ in range(K+1)]
# def bfs(i):
#     willvisit = deque()
#     willvisit.append((i, 0))
#     isinqueue[i] = True
#     while willvisit:
#         now = willvisit.popleft()
#         i, depth = now
#         if i == K:
#             return depth
#         else:
#             if len(graph[i]) == 1 and graph[i][0] != 100:
#                 # if not isinqueue[graph[i][0]]:
#                 willvisit.appendleft((graph[i][0], depth))
#                 isinqueue[graph[i][0]] = True
#             else:
#                 for node in graph[i]:
#                     if not isinqueue[node]:
#                         willvisit.append((node, depth+1))
#                         isinqueue[node] = True
#
# print(bfs(1))

from sys import stdin
from collections import deque
K = 100
graph = [[] for i in range(K+1)]
for i in range(1, K+1):
    for dice in range(1, 6+1):
        if i < K-dice+1:
            graph[i].append(i+dice)
N, M = map(int, stdin.readline().rstrip().split(" "))
for _ in range(N):
    x, y = map(int, stdin.readline().rstrip().split(" "))
    graph[x] = [y]
for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split(" "))
    graph[u] = [v]

isinqueue = [0 for _ in range(K+1)]
def bfs(i):
    willvisit = deque()
    willvisit.append((i, 0))
    isinqueue[i] = True
    while willvisit:
        now = willvisit.popleft()
        i, depth = now
        if i == K:
            return depth
        else:
            if len(graph[i]) == 1 and graph[i][0] != 100:
                if not isinqueue[graph[i][0]] or isinqueue[graph[i][0]] > depth :
                    willvisit.appendleft((graph[i][0], depth))
                    isinqueue[graph[i][0]] = depth
            else:
                for node in graph[i]:
                    if not isinqueue[node]:
                        willvisit.append((node, depth+1))
                        isinqueue[node] = depth + 1

print(bfs(1))