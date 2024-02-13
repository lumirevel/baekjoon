from sys import stdin
from queue import PriorityQueue
N, M = map(int, stdin.readline().split(" "))
adjList = []
for _ in range(N):
    adjList.append([])
for _ in range(M):
    v, w = map(int, stdin.readline().split(" "))
    adjList[v-1].append(w-1)

orderedList = PriorityQueue()
time = 0
forwardVisited = [False] * N
stack = []
for i in range(N):
    stack.append(i)
    while stack:
        now = stack.pop()
        forwardVisited[now] = True

        time += 1
        orderedList.put((-time, now))
        for next in adjList[now]:
            if not forwardVisited[next]:
                stack.append(next)

visitCount = 0
backwardVisited = [False] * N
stack = [orderedList.get()[1]]
while stack:
    now = stack.pop()
    backwardVisited[now] = True
    visitCount += 1
    for next in adjList[now]:
        if not backwardVisited[next]:
            stack.append(next)

if visitCount == N:
    print("Yes")
else:
    print("No")