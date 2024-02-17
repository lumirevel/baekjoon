from collections import deque
M, N, K = map(int, input().split(" "))
squareList = []
for _ in range(K):
    lowerX, lowerY, upperX, upperY = map(int, input().split(" "))
    squareList.append(((lowerX, lowerY), (upperX, upperY)))


isColored = []
for x in range(N):
    isColored.append([])
    for y in range(M):
        isColored[x].append(False)
for lower, upper in squareList:
    lowerX, lowerY = lower
    upperX, upperY = upper
    for x in range(lowerX, upperX):
        for y in range(lowerY, upperY):
            isColored[x][y] = True

visited = []
for x in range(N):
    visited.append([])
    for y in range(M):
        visited[x].append(False)
countList = []
for x in range(N):
    for y in range(M):
        value = 0
        waitingList = deque([(x,y)])
        while waitingList:
            nowX, nowY = waitingList.popleft()
            if not visited[nowX][nowY] and not isColored[nowX][nowY]:
                visited[nowX][nowY] = True
                value += 1
                if nowX-1 >= 0:
                    waitingList.append((nowX-1, nowY))
                if nowX+1 < N:
                    waitingList.append((nowX+1, nowY))
                if nowY-1 >= 0:
                    waitingList.append((nowX,  nowY-1))
                if nowY+1 < M:
                    waitingList.append((nowX,  nowY+1))

        if value != 0:
            countList.append(value)


print(len(countList))
for count in sorted(countList):
    print(count, end=" ")
