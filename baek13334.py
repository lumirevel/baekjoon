from sys import stdin
from queue import PriorityQueue

N = int(input())

lines = []
for _ in range(N):
    ho = list(map(int, stdin.readline().split(" ")))
    lines.append((min(ho), max(ho)))
lines.sort(key = lambda x:x[1])
D = int(input())

# 집어 넣고
# 거리를 보면서 뺀다

# 끝을 기준으로 정렬하고
# 하나씩 빼면서
# 시작점을 기준으로 heap 사용
maxPeople = 0
onRail = PriorityQueue()
for line in lines:
    if line[1] - line[0] <= D:
        if not onRail.empty() and onRail.queue[0] < line[1] - D:
            onRail.get()
        onRail.put(line[0])
    if maxPeople < onRail.qsize():
        maxPeople = onRail.qsize()

print(maxPeople)
