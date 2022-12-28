# from sys import stdin, setrecursionlimit
# setrecursionlimit(100000)
# N, M = map(int, stdin.readline().rstrip().split(" "))
# maze = []
# for _ in range(N):
#     maze.append([])
#     for v in stdin.readline().rstrip():
#         maze[-1].append(int(v))
# visited = [[M*N+1 for _ in range(M)] for _ in range(N)]
#
# def dfs(pos, depth):
#     i, j = pos
#     if visited[i][j] > depth:
#         visited[i][j] = depth
#         if i != 0:
#             if maze[i-1][j]:
#                 dfs((i-1, j), depth+1)
#         if i != N-1:
#             if maze[i+1][j]:
#                 dfs((i+1, j), depth+1)
#         if j != 0:
#             if maze[i][j-1]:
#                 dfs((i, j-1), depth+1)
#         if j != M-1:
#             if maze[i][j+1]:
#                 dfs((i, j+1), depth+1)
#
# dfs((0,0), 1)
# print(visited[N-1][M-1])

from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().rstrip().split(" "))
maze = []
for _ in range(N):
    maze.append([])
    for v in stdin.readline().rstrip():
        maze[-1].append(int(v))

isinqueue = [[False for _ in range(M)] for _ in range(N)]
def bfs(pos, depth):
    willvisit = deque()
    willvisit.append((pos, depth))
    i, j = pos
    isinqueue[i][j] = True
    while willvisit:
        now = willvisit.popleft()
        pos, depth = now
        i, j = pos
        if i == N - 1 and j == M - 1:
            return depth
        else:
            if i != 0:
                if maze[i-1][j]:
                    if not isinqueue[i-1][j]:
                        willvisit.append(((i-1, j), depth+1))
                        isinqueue[i-1][j] = True
            if i != N-1:
                if maze[i+1][j]:
                    if not isinqueue[i+1][j]:
                        willvisit.append(((i+1, j), depth+1))
                        isinqueue[i+1][j] = True
            if j != 0:
                if maze[i][j-1]:
                    if not isinqueue[i][j-1]:
                        willvisit.append(((i, j-1), depth+1))
                        isinqueue[i][j-1] = True
            if j != M-1:
                if maze[i][j+1]:
                    if not isinqueue[i][j+1]:
                        willvisit.append(((i, j+1), depth+1))
                        isinqueue[i][j+1] = True

print(bfs((0, 0), 1))