from sys import setrecursionlimit
setrecursionlimit(20000)
N = int(input())
memo = []
stepMap = []
for _ in range(N):
    stepMap.append(list(map(int, input().split(" "))))
    memo.append([None] * N)

def move(stepMap, i, j, N):
    if i >= N or j >= N:
        return 0
    if i == N-1 and j == N-1:
        return 1
    count = memo[i][j]
    if count is None:
        step = stepMap[i][j]
        memo[i][j] = move(stepMap, i+step, j, N) + move(stepMap, i, j+step, N)
        return memo[i][j]
    return count

print(move(stepMap, 0, 0, N))