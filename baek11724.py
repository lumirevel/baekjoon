# 내 version

# from sys import stdin, setrecursionlimit
# setrecursionlimit(10000)
#
# N, M = map(int, stdin.readline().rstrip().split(" "))
#
# tree = dict()
# for i in range(N):
#     tree[i+1] = []
# for _ in range(M):
#     u, v = map(int, stdin.readline().rstrip().split(" "))
#     tree[u].append(v)
#     tree[v].append(u)
#
# visited = []
# loopcount = 0
# def DFS(i):
#     global loopcount
#     visited.append(i)
#     restchildren = set(tree[i]) - set(visited)
#     if len(restchildren) == 0:
#         pass
#     else:
#         for i in restchildren:
#             if i not in visited:
#                 DFS(i)
#
# unvisited = set(tree.keys())-set(visited)
# while unvisited:
#     DFS(list(unvisited)[0])
#     loopcount += 1
#     unvisited = set(tree.keys()) - set(visited)
#
# print(loopcount)

# 성범 version
from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

N, M = map(int, stdin.readline().rstrip().split(" "))

tree = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split(" "))
    tree[u].append(v)
    tree[v].append(u)

visited = [False for _ in range(N+1)]
def DFS(i):
    visited[i] = True
    for next in tree[i]:
        if not visited[next]:
            DFS(next)

loopcount = 0
for i in range(N):
    if not visited[i + 1]:
        DFS(i + 1)
        loopcount += 1

print(loopcount)
