from queue import PriorityQueue
V, E = map(int, input().split(" "))
adjList = []
for _ in range(V):
    adjList.append([])
for _ in range(E):
    a, b, c = map(int, input().split(" "))
    adjList[a-1].append((b-1, c))


def transformedDijkstra(start):
    shortestList = [float('inf')] * V
    shortestList[start] = 0
    waitingList = PriorityQueue()
    waitingList.put((0, start))
    minCycle = float('inf')
    while waitingList.queue:
        distance, node = waitingList.get()
        if shortestList[node] < distance:
            continue
        for v, w in adjList[node]:
            newDistance = distance + w
            if v == start and newDistance < minCycle:
                minCycle = newDistance
            if newDistance < shortestList[v]:
                shortestList[v] = newDistance
                waitingList.put((newDistance, v))
    return minCycle

minCycle = float('inf')
for i in range(V):
    value = transformedDijkstra(i)
    if value < minCycle:
        minCycle = value


if minCycle != float('inf'):
    print(minCycle)
else:
    print(-1)
