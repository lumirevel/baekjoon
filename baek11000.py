from sys import stdin
from queue import PriorityQueue

N = int(input())
lectureList = []
for _ in range(N):
    lectureList.append(list(map(int, stdin.readline().split(" "))))
lectureList.sort(key = lambda x:x[0])

count = 0
simultaneity = PriorityQueue()
for lecture in lectureList:
    S,T = lecture
    while simultaneity.queue and simultaneity.queue[0] <= S:
        simultaneity.get()
    simultaneity.put(T)
    count = max(count, len(simultaneity.queue))

print(count)
