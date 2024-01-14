N = int(input())

colorCosts = []
for _ in range(N):
    colorCosts.append(tuple(map(int, input().split(" "))))

DP = []
for _ in range(3):
    DP.append([])
    for _ in range(3):
        DP[-1].append(float('inf'))
for i in range(N):
    R, G, B = colorCosts[i]
    if i == 0:
        for j in range(3):
            DP[j][j] = colorCosts[i][j]
    elif i == N-1:
        for j in range(3):
            prevR, prevG, prevB = DP[j]
            if j != 0:
                DP[j][0] = min(prevG, prevB) + R
            if j != 1:
                DP[j][1] = min(prevR, prevB) + G
            if j != 2:
                DP[j][2] = min(prevR, prevG) + B
    else:
        for j in range(3):
            prevR,prevG,prevB = DP[j]

            DP[j][0] = min(prevG, prevB) + R
            DP[j][1] = min(prevR, prevB) + G
            DP[j][2] = min(prevR, prevG) + B

print(min(DP[0][1], DP[0][2], DP[1][0], DP[1][2], DP[2][0], DP[2][1]))