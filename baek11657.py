N, M = map(int, input().split(" "))
edge = []
for _ in range(M):
    A, B, C = map(int, input().split(" "))
    edge.append((A-1, B-1, C))


shortestList = [float("inf")] * N
def bellmanFord(start = 0):
    shortestList[start] = 0

    for _ in range(N-1):
        for u, v, w in edge:
            newDistance = shortestList[u] + w
            if newDistance < shortestList[v]:
                shortestList[v] = newDistance
    for u, v, w in edge:
        if shortestList[u] + w < shortestList[v]:
            return False
    return True


if bellmanFord():
    for shortest in shortestList[1:]:
        if shortest != float("inf"):
            print(shortest)
        else:
            print(-1)
else:
    print(-1)
