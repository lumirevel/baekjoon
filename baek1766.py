from sys import setrecursionlimit, stdin
from queue import PriorityQueue
setrecursionlimit(100005)


N, M = map(int, stdin.readline().split(" "))
adjList = []
for _ in range(N):
    adjList.append([])
inDegreeList = [0] * N
for _ in range(M):
    A, B = map(int, stdin.readline().split(" "))
    adjList[A-1].append(B-1)
    inDegreeList[B-1] += 1


waitingList = PriorityQueue()
for i in range(N):
    if inDegreeList[i] == 0:
        waitingList.put(i)
sortedList = []
while waitingList.queue:
    now = waitingList.get()
    sortedList.append(now+1)
    for child in adjList[now]:
        inDegreeList[child] -= 1
        if inDegreeList[child] == 0:
            waitingList.put(child)


for number in sortedList:
    print(number, end=" ")
