N, M = map(int, input().split(" "))
sumArray = []
for i in range(N):
    sumArray.append(list(map(int, input().split(" "))))
    cumulatedSum = 0
    for j in range(N):
        cumulatedSum += sumArray[i][j]
        if i == 0:
            sumArray[i][j] = cumulatedSum
        else:
            sumArray[i][j] = cumulatedSum + sumArray[i-1][j]
for _ in range(M):
    x1,y1, x2,y2 = list(map(int, input().split(" ")))
    result = sumArray[x2-1][y2-1]
    if x1 != 1 and y2 != 0:
        result -= sumArray[x1-2][y2-1]
    if x2 != 0 and y1 != 1:
        result -= sumArray[x2-1][y1-2]
    if x1 != 1 and y1 != 1:
        result += sumArray[x1-2][y1-2]
    print(result)
