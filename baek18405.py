# from sys import stdin
# from copy import deepcopy as copy
#
# N, K = map(int, stdin.readline().split(" "))
#
# plate = []
# for n in range(N):
#     plate.append(list(map(int, stdin.readline().split(" "))))
# S, X, Y = map(int, stdin.readline().split(" "))
#
# # 바이러스 탐색
# AP = dict()
# for k in range(1, K+1):
#     AP[k] = []
#
# for i in range(N):
#     for j in range(N):
#         if plate[i][j] != 0:
#             AP[plate[i][j]].append((i,j))
#
# # BFS & Simulation
# end = True
# for _ in range(S):
#     newVirus = dict()
#     for k in range(1, K + 1):
#         newVirus[k] = []
#     for v in range(1, K+1):
#         while len(AP[v]):
#             i,j = AP[v].pop(-1)
#             if not i == 0:
#                 if plate[i - 1][j] == 0:
#                     plate[i - 1][j] = v
#                     newVirus[v].append((i-1,j))
#                     end = False
#             if not i == N - 1:
#                 if plate[i + 1][j] == 0:
#                     plate[i + 1][j] = v
#                     newVirus[v].append((i+1,j))
#                     end = False
#             if not j == 0:
#                 if plate[i][j - 1] == 0:
#                     plate[i][j - 1] = v
#                     newVirus[v].append((i,j-1))
#                     end = False
#             if not j == N - 1:
#                 if plate[i][j + 1] == 0:
#                     plate[i][j + 1] = v
#                     newVirus[v].append((i,j+1))
#                     end = False
#     if end:
#         break
#     AP = copy(newVirus)
#
# # result
# print(plate[X-1][Y-1])

from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split(" "))

plate = []
for n in range(N):
    plate.append(list(map(int, stdin.readline().split(" "))))
S, X, Y = map(int, stdin.readline().split(" "))

# 바이러스 탐색
virus = dict()
for k in range(1, K+1):
    virus[k] = deque()

for i in range(N):
    for j in range(N):
        if plate[i][j] != 0:
            virus[plate[i][j]].append((i,j))

# BFS & Simulation
end = True
for _ in range(S):
    for v in range(1, K+1):
        for _ in range(len(virus[v])):
            i,j = virus[v].popleft()
            if not i == 0:
                if plate[i - 1][j] == 0:
                    plate[i - 1][j] = v
                    virus[v].append((i-1,j))
                    end = False
            if not i == N - 1:
                if plate[i + 1][j] == 0:
                    plate[i + 1][j] = v
                    virus[v].append((i+1,j))
                    end = False
            if not j == 0:
                if plate[i][j - 1] == 0:
                    plate[i][j - 1] = v
                    virus[v].append((i,j-1))
                    end = False
            if not j == N - 1:
                if plate[i][j + 1] == 0:
                    plate[i][j + 1] = v
                    virus[v].append((i,j+1))
                    end = False
    if end:
        break

# result
print(plate[X-1][Y-1])