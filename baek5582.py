A = input()
B = input()

DP = []
for _ in range(len(B)):
    DP.append([])
    for _ in range(len(A)):
        DP[-1].append(0)

maxCount = 0
for i, b in enumerate(B):
    for j, a in enumerate(A):
        if a == b:
            prev = 0
            if i != 0 and j != 0:
                prev = DP[i-1][j-1]
            DP[i][j] = prev + 1
            if maxCount < DP[i][j]:
                maxCount = DP[i][j]

print(maxCount)
