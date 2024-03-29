from sys import stdin, setrecursionlimit
from queue import PriorityQueue
setrecursionlimit(200005)
N, M = map(int, stdin.readline().split(" "))
forwardAdjList = []
backwardAdjList = []
for _ in range(N):
    forwardAdjList.append([])
    backwardAdjList.append([])
for _ in range(M):
    v, w = map(int, stdin.readline().split(" "))
    forwardAdjList[v-1].append(w-1)
    backwardAdjList[w-1].append(v-1)

orderedList = PriorityQueue()
forwardVisited = [False] * N
def forwardDFS(now, time):
    forwardVisited[now] = True

    time += 1
    for next in forwardAdjList[now]:
        if not forwardVisited[next]:
            time = forwardDFS(next, time)
    time += 1
    orderedList.put((-time, now))
    return time
time = 0
for i in range(N):
    if not forwardVisited[i]:
        time = forwardDFS(i, time)

backwardVisited = [False] * N
def backwardDFS(now):
    backwardVisited[now] = True
    visitCount = 1
    for next in backwardAdjList[now]:
        if not backwardVisited[next]:
            visitCount += backwardDFS(next)
    return visitCount

if backwardDFS(orderedList.get()[1]) == N:
    print("Yes")
else:
    print("No")
