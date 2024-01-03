from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())

buildings = []
for _ in range(N):
    buildings.append(tuple(map(int, stdin.readline().split(" "))))
buildings.sort(key = lambda x:x[0])

tray = PriorityQueue()
changes = []
for building in buildings:
    L, H, R = building
    if not tray.empty():
        maxR = tray.queue[0][1]
        while not tray.empty() and tray.queue[0][1] < L:
            nowMH, nowR = tray.get()

            if maxR < nowR:# 떨어져 도착한 높이(-nowMH)를 떨어진 위치(maxR)로 기록해야함
                changes.append((maxR, -nowMH))
                maxR = nowR

        if tray.empty():# 떨어졌는데 바닥이 없는 경우
            changes.append((maxR, 0))
        elif maxR != tray.queue[0][1]:
            changes.append((maxR, -tray.queue[0][0]))

    tray.put((-H,R))
    if -tray.queue[0][0] == H:
        changes.append((L, H))

# 모두 뽑아야 하기 때문에
maxR = tray.queue[0][1]
while not tray.empty():
    nowMH, nowR = tray.get()
    if maxR < nowR:# 떨어져 도착한 높이(-nowMH)를 떨어진 위치(maxR)로 기록해야함
        changes.append((maxR, -nowMH))
        maxR = nowR
if tray.empty():# 떨어졌는데 바닥이 없는 경우
    changes.append((maxR, 0))
elif maxR != tray.queue[0][1]:
    changes.append((maxR, -tray.queue[0][0]))

result = ""
for change in changes:
    result += f"{change[0]} {change[1]} "
print(result[0:-1])