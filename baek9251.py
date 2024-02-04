A = input()
B = input()

DP = []
for i, a in enumerate(A):
    DP.append([])
    if i == 0:
        for j, b in enumerate(B):
            if j == 0:
                DP[i].append(int(a == b))
            else:
                DP[i].append(max(DP[i][j-1], int(a == b)))
    else:
        for j, b in enumerate(B):
            if j == 0:
                DP[i].append(max(DP[i-1][j], int(a == b)))
            elif a == b:
                DP[i].append(max(DP[i][j-1], DP[i-1][j-1]+1))
            else:
                DP[i].append(max(DP[i][j-1], DP[i-1][j]))

print(DP[-1][-1])
