from sys import stdin

N = int(stdin.readline())

matrixSizes = []
for _ in range(N):
    matrixSizes.append(tuple(map(int, stdin.readline().split(" "))))

minCal = [[None for _ in range(len(matrixSizes))] for _ in range(len(matrixSizes))]

for alpha in range(len(matrixSizes)):
    for i in range(len(matrixSizes)):
        if alpha == 0:
            minCal[i][i + alpha] = 0
        else:
            if i + alpha < len(matrixSizes):
                minNow = None
                for j in range(i, i + alpha):
                    now = minCal[i][j] + matrixSizes[i][0]*matrixSizes[j][1]*matrixSizes[i + alpha][1] + minCal[j+1][i + alpha]
                    if minNow == None:
                        minNow = now
                    elif minNow > now:
                        minNow = now
                minCal[i][i+alpha] = minNow

print(minCal[0][len(matrixSizes)-1])

