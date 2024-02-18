from sys import setrecursionlimit, stdin
from queue import PriorityQueue
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
doneParentCountList = [0] * N
for i in range(N):
    waitingList = PriorityQueue()
    waitingList.put(i)
    while waitingList.queue:
        now = waitingList.get()
        if doneParentCountList[now] == len(reverseAdjList[now]):
            # 자식에게서 다시 자신이 나오려면 cycle이 존재해야하는데 이는 Topology Sort에 모순이다.
            sortedList.append(now+1)
            for child in adjList[now]:
                # 이미 sortedList에 추가된 자식이 이곳에 도착하려면 자식의 처리 안 된 parent가 존재하면 안되는데 방금 직전까지 존재했으므로 모순이다.
                doneParentCountList[child] += 1
                if child < i:
                    waitingList.put(child)


for number in sortedList:
    print(number, end=" ")
