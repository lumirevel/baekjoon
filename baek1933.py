from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())

buildings = [(1000000001,0,1000000001)]
for _ in range(N):
    buildings.append(tuple(map(int, stdin.readline().split(" "))))
buildings.sort(key = lambda x:x[0])

tray = PriorityQueue()
changes = PriorityQueue()
for building in buildings:
    L, H, R = building
    if not tray.empty():
        maxR = tray.queue[0][1]
        while not tray.empty() and tray.queue[0][1] < L:
            nowMH, nowR = tray.get()

            if maxR < nowR:
                changes.put((maxR, -nowMH))
                maxR = nowR

        if tray.empty():
            changes.put((maxR, 0))
        elif maxR != tray.queue[0][1]:
            changes.put((maxR, -tray.queue[0][0]))

    tray.put((-H,R))
    if tray.queue[0][0] != 0 and -tray.queue[0][0] == H:
        changes.put((L, H))

result = "basement: "
while(not changes.empty()):
    change = changes.get()
    result += f"{change[0]} {change[1]} "
print(result[0:-1])