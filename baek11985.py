from sys import stdin
N, M, K = map(int, stdin.readline().split(" "))
orangeList = []
for _ in range(N):
    orangeList.append(int(stdin.readline()))

DP = []
maxDP = []
minDP = []
for _ in range(N):
    DP.append([float('inf')] * N)
    maxDP.append([0] * N)
    minDP.append([float('inf')] * N)

for j in range(N):
    for i in range(N-j):
        if j == 0:
            maxDP[i][j] = orangeList[i]
            minDP[i][j] = orangeList[i]
            DP[i][j] = K
        else:
            maxDP[i][j] = max(maxDP[i][j-1], maxDP[i+j][0])
            minDP[i][j] = min(minDP[i][j-1], minDP[i+j][0])
            if j < M:
                DP[i][j] = min(DP[i][j-1]+DP[i+j][0], K + (j+1)*(maxDP[i][j] - minDP[i][j]), DP[i][0]+DP[i+1][j-1])
            else:
                minValue = float('inf')
                for inter in range(j):
                    minValue = min(minValue, DP[i][inter]+DP[i+inter+1][j-inter-1])
                DP[i][j] = minValue

print(DP[0][-1])
