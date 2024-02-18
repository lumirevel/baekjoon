from collections import deque


T = int(input())
testCaseList = []
for _ in range(T):
    l = int(input())
    startPoint = tuple(map(int, input().split(" ")))
    endPoint = tuple(map(int, input().split(" ")))
    testCaseList.append((l, startPoint, endPoint))


for l, startPoint, endPoint in testCaseList:
    stateList = []
    for x in range(l):
        stateList.append([])
        for y in range(l):
            stateList[x].append(0)
    waitingList = deque()
    waitingList.append((startPoint, 0))
    while waitingList:
        nowPoint, count = waitingList.popleft()
        nowX, nowY = nowPoint
        stateList[nowX][nowY] = 2

        if nowPoint == endPoint:
            print(count)
            break
        else:
            newPointList = [(nowX-2, nowY+1), (nowX-1, nowY+2), (nowX+1, nowY+2), (nowX+2, nowY+1),
                            (nowX-2, nowY-1), (nowX-1, nowY-2), (nowX+1, nowY-2), (nowX+2, nowY-1)]
            for newPoint in newPointList:
                newX, newY = newPoint
                if 0 <= newX < l and 0<= newY < l and stateList[newX][newY] == 0:
                    stateList[newX][newY] = 1
                    waitingList.append((newPoint, count+1))
