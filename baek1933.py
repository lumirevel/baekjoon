from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())

buildings = []
for _ in range(N):
    buildings.append(tuple(map(int, stdin.readline().split(" "))))
buildings.sort(key = lambda x:x[1])

currentHeight = None
layers = []
for building in buildings:
    if currentHeight != building[1]:
        currentHeight = building[1]
        layers.append([])
    layers[-1].append(building)

buildingLines = []
for layer in layers:
    layer.sort(key=lambda x: x[0])

    startPoint = None
    endPoint = None
    height = None
    for building in layer:
        if startPoint is None:
            startPoint = building[0]
        if height is None:
            height = building[1]
        if endPoint is None:
            endPoint = building[2]

        if endPoint < building[0]:
            buildingLines.append((startPoint, height, endPoint))
            startPoint = building[0]
            endPoint = building[2]
        elif endPoint < building[2]:
            endPoint = building[2]
    buildingLines.append((startPoint, height, endPoint))
buildingLines.append((1000000001, 0, 1000000001)) # 전부 빼기 위함
buildingLines.sort(key = lambda x:x[0])

tray = PriorityQueue() # max heap으로 하기 위해 음수로 저장할 것
changes = []
for buildingLine in buildingLines:
    L, H, R = buildingLine
    prvH = 0
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
        if changes and changes[-1][1] == L and changes[-1][1] < H:
            changes.pop()
        changes.append((L, H))

result = ""
for change in changes:
    result += f"{change[0]} {change[1]} "
print(result[0:-1])