V, E = map(int, input().split(" "))
W = []
for i in range(V):
    W.append([])
    for j in range(V):
        W[i].append(float('inf'))
for _ in range(E):
    a, b, c = map(int, input().split(" "))
    W[a-1][b-1] = c


def transformedFloadWashall(W):
    n = len(W)
    D = W
    for k in range(n):
        newD = []
        for i in range(n):
            newD.append([])
            for j in range(n):
                newD[i].append(min(D[i][j], D[i][k]+D[k][j]))
        D = newD
    minCycle = float('inf')
    for i in range(n):
        minCycle = min(minCycle, D[i][i])
    return minCycle
minCycle = transformedFloadWashall(W)


if minCycle != float('inf'):
    print(minCycle)
else:
    print(-1)
