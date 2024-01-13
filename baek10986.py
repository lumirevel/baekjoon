from sys import stdin
N, M = map(int, stdin.readline().split(" "))
A = list(map(int, stdin.readline().split(" ")))

DP = []
for _ in range(M):
    DP.append(0)

count = 0
base = 0
for Ai in A:
    r = Ai % M
    DP[base] += 1
    base -= r
    base %= M
    count += DP[base]

print(count)
