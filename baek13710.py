# from sys import stdin
#
# N = int(stdin.readline())
# bits = [[] for _ in range(N)]
# result = [0 for _ in range(30)]
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     while cache:
#         bits[i].append(cache % 2)
#         cache //= 2
#     for i, v in enumerate(bits[i]):
#         if result[i] + v == 1:
#             result[i] = 1
#         else:
#             result[i] = 0
#
# print(result)

# from sys import stdin
#
# N = int(stdin.readline())
# bits = [[] for _ in range(N)]
# result = [[[0 for _ in range(30)] for _ in range(N)] for _ in range(N)]
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     while cache:
#         bits[i].append(cache % 2)
#         cache //= 2
#
# sum = 0
#
# for alpha in range(N):
#     for i in range(N):
#         if i+alpha < N:
#             for p, v in enumerate(bits[i+alpha]):
#                 if result[i][i+alpha-1][p] + v == 1:
#                     result[i][alpha][p] = 1
#                 else:
#                     result[i][alpha][p] = 0
#             # result[i][i+alpha]=result[i][i+alpha-1]***bits[i+alpha]
#             now = 1
#             for v in result[i][alpha]:
#                 sum += v * now
#                 now *= 2
#
# print(sum)

# from sys import stdin
#
# N = int(stdin.readline())
# bits = [[] for _ in range(N)]
# result = [[0 for _ in range(30)] for _ in range(N)]
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     while cache:
#         bits[i].append(cache % 2)
#         cache //= 2
#
# sum = 0
#
# for alpha in range(N):
#     for i in range(N):
#         if i+alpha < N:
#             for p, v in enumerate(bits[i+alpha]):
#                 if result[i][p] + v == 1:
#                     result[i][p] = 1
#                 else:
#                     result[i][p] = 0
#             # result[i][i+alpha]=result[i][i+alpha-1]***bits[i+alpha]
#             now = 1
#             for v in result[i]:
#                 sum += v * now
#                 now *= 2
#
# print(sum)

# from sys import stdin
#
# N = int(stdin.readline())
# bits = [[] for _ in range(N)]
# result = [[0 for _ in range(30)] for _ in range(N)]
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     while cache:
#         bits[i].append(cache % 2)
#         cache //= 2
#
# sum = 0
#
# for alpha in range(N):
#     for i in range(N):
#         if i+alpha < N:
#             now = 1
#             for p, v in enumerate(bits[i+alpha]):
#                 if result[i][p] + v == 1:
#                     result[i][p] = 1
#                     sum += now
#                 else:
#                     result[i][p] = 0
#                 now *= 2
#             # result[i][i+alpha]=result[i][i+alpha-1]***bits[i+alpha]
#
# print(sum) # 생각해보니 잘못된 알고리즘이다.

# from sys import stdin
#
# N = int(stdin.readline())
# bits = [[] for _ in range(N)]
# result = [[0 for _ in range(30)] for _ in range(N)]
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     while cache:
#         bits[i].append(cache % 2)
#         cache //= 2
#
# sum = 0
#
# for alpha in range(N):
#     for i in range(N):
#         if i+alpha < N:
#             now = 1
#             for p, v in enumerate(bits[i+alpha]):
#                 if result[i][p] + v == 1:
#                     result[i][p] = 1
#                     sum += now
#                 else:
#                     result[i][p] = 0
#                 now *= 2
#             for p in (len(bits[i+alpha]),len(result[i])):
#                 sum += now * result[i][p]
#                 now *= 2
#             # result[i][i+alpha]=result[i][i+alpha-1]***bits[i+alpha]
#
# print(sum)//제출 x

# from sys import stdin
#
# N = int(stdin.readline())
# bytes = [[] for _ in range(N)]
# summary = [0]
# a = 1
# for n in range(1, N+1):
#     summary.append(a)
#     a *= 2
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     while cache:
#         bytes[i].append(cache % 2)
#         cache //= 2
#
# count = [0 for _ in range(N)]
# for byte in bytes:
#     for i, bit in enumerate(byte):
#         count[i] += bit
#
# sum = 0
# a=1
# for i, cnt in enumerate(count):
#     sum += summary[cnt]*a
#     a *= 2
#
# print(sum) # 아이디어

# from sys import stdin
#
# N = int(stdin.readline())
# whens = [[] for _ in range(30)]
# raws = list(map(int, stdin.readline().split(" ")))
#
# for i in range(N):
#     cache = raws[i]
#     bit = 0
#     while cache:
#         if cache % 2:
#             whens[bit].append(i)
#         cache //= 2
#         bit += 1
#
# print(whens) # 아이디어

from sys import stdin
N = int(stdin.readline())
raws = list(map(int, stdin.readline().split(" ")))

bytes = [[] for _ in range(N)]
for i in range(N):
    cache = raws[i]
    while cache:
        bytes[i].append(cache % 2)
        cache //= 2

process = [[[0,0] for _ in range(30)] for _ in range(N)]# [[[홀, 짝] * 30] * N(단계수)]
sumBit = [0 for _ in range(30)]
for n, byte in enumerate(bytes):
    for i in range(30):
        if i < len(byte):
            bit = byte[i]
        else:
            bit = 0

        if n == 0:
            if bit:
                process[n][i][0] += 1
            else:
                process[n][i][1] += 1
            sumBit[i] += process[n][i][0]
        else:
            if bit:
                process[n][i][0], process[n][i][1] = process[n-1][i][1] + 1, process[n-1][i][0]
            else:
                process[n][i][0], process[n][i][1] = process[n-1][i][0], process[n-1][i][1] + 1
            sumBit[i] += process[n][i][0]

an = 1
result = 0
for bit in sumBit:
    result += bit * an
    an *= 2

print(result)