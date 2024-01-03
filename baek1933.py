from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())

buildings = [(1000000001, 0, 1000000001)] # 전부 빼기 위함
for _ in range(N):
    buildings.append(tuple(map(int, stdin.readline().split(" "))))
buildings.sort(key = lambda x:x[0])

tray = PriorityQueue() # max heap으로 하기 위해 음수로 저장할 것
changes = []
for building in buildings:
    L, H, R = building
    if not tray.empty():
        maxR = tray.queue[0][1]
        while not tray.empty() and tray.queue[0][1] < L:
            nowMH, nowR = tray.get()

            if maxR < nowR: # 떨어져 도착한 높이(-nowMH)를 떨어진 위치(maxR)로 기록해야함
                changes.append((maxR, -nowMH))
                maxR = nowR
        if tray.empty(): # 떨어졌는데 건물이 없는 경우
            changes.append((maxR, 0))
        elif maxR != tray.queue[0][1]: # 범위가 L보다 오른쪽까지 있는 바닥인 경우
            changes.append((maxR, -tray.queue[0][0]))

    tray.put((-H,R))
    if tray.queue[0][0] != 0 and -tray.queue[0][0] == H:
        changes.append((L, H))

result = ""
for change in changes:
    result += f"{change[0]} {change[1]} "
print(result[0:-1])