from sys import stdin
N, M, K = map(int, stdin.readline().split(" "))
orangeList = []
for _ in range(N):
    orangeList.append(int(stdin.readline()))

maxDP = []
minDP = []
for _ in range(N):
    maxDP.append([0] * M)
    minDP.append([float('inf')] * M)

for j in range(M):
    for i in range(N-j):
        if j == 0:
            maxDP[i][j] = orangeList[i]
            minDP[i][j] = orangeList[i]
        else:
            maxDP[i][j] = max(maxDP[i][j-1], maxDP[i+j][0])
            minDP[i][j] = min(minDP[i][j-1], minDP[i+j][0])

resultBoard = [float('inf')] * N
for i in range(N):
    if i == 0:
        resultBoard[i] = K
    elif i < M:
        resultBoard[i] = K + (i+1)*(maxDP[0][i] - minDP[0][i])
        for j in range(i):
            resultBoard[i] = min(resultBoard[i], resultBoard[i-j-1] + K + (j+1)*(maxDP[i-j][j] - minDP[i-j][j]))
    else:
        for j in range(M):
            resultBoard[i] = min(resultBoard[i], resultBoard[i-j-1] + K + (j+1)*(maxDP[i-j][j] - minDP[i-j][j]))

print(resultBoard[-1])
