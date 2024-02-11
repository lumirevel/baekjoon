from collections import deque
n, w, L = map(int, input().split(" "))
truckList = list(map(int, input().split(" ")))

onBridge = deque()
onBridgeWeight = 0
time = 0
i = 0
while i < len(truckList):
    truckWeight = truckList[i]
    if len(onBridge) == w:
        onBridgeWeight -= onBridge.popleft()
    if onBridgeWeight + truckWeight <= L:
        onBridge.append(truckWeight)
        onBridgeWeight += truckWeight
        i += 1
    else:
        onBridge.append(0)
    time += 1
while onBridgeWeight != 0:
    if len(onBridge) == w:
        onBridgeWeight -= onBridge.popleft()
    onBridge.append(0)
    time += 1

print(time)