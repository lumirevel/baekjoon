from sys import stdin
from queue import PriorityQueue
N = int(stdin.readline())
A, B, C = map(int, stdin.readline().split(" "))
M = int(stdin.readline())
adjList = []
for _ in range(N):
    adjList.append([])
for _ in range(M):
    D, E, L = map(int, stdin.readline().split(" "))
    adjList[D-1].append((E-1, L))


def dijkstra(home):
    fromHome = [float("inf")] * N
    fromHome[home] = 0

    waitingList = PriorityQueue()
    waitingList.put((0, home))
    while waitingList.queue:
        distance, now = waitingList.get()
        if fromHome[now] < distance:
            continue
        for child, l in adjList[now]:
            newDistance = distance + l
            if newDistance < fromHome[child]:
                fromHome[child] = newDistance
                waitingList.put((newDistance, child))

    return fromHome

fromA = dijkstra(A-1)
fromB = dijkstra(B-1)
fromC = dijkstra(C-1)

farthestValue = 0
farthestPlace = 0
for i in range(N):
    distance = min(fromA[i], fromB[i], fromC[i])
    if farthestValue < distance:
        farthestValue = distance
        farthestPlace = i+1


print(farthestPlace)
