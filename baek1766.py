from sys import setrecursionlimit, stdin
from queue import PriorityQueue
from collections import deque
setrecursionlimit(100005)
N, M = map(int, stdin.readline().split(" "))
adjList = []
reverseAdjList = []
for _ in range(N):
    adjList.append([])
    reverseAdjList.append([])
for _ in range(M):
    A, B = map(int, stdin.readline().split(" "))
    adjList[A-1].append(B-1)
    reverseAdjList[B-1].append(A-1)


for subList in adjList:
    subList.sort()
sortedList = []
isAddedList = [False] * N
parentOKList = [0] * N
for i in range(N):
    if not isAddedList[i]:
        waitingList = PriorityQueue()
        waitingList.put(i)
        while waitingList.queue:
            now = waitingList.get()
            if parentOKList[now] == len(reverseAdjList[now]):
                sortedList.append(now+1)
                for child in adjList[now]:
                    parentOKList[child] += 1
                    if child <= i:
                        waitingList.put(child)


for number in sortedList:
    print(number, end=" ")
