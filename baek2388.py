N, M = map(int, input().split(" "))

def binarySearch(lst, item):
    start = 0
    end = len(lst) - 1
    mid = (start + end) // 2
    while lst[mid] != item:
        now = lst[mid]
        if item < now:
            end = mid - 1
        elif item > now:
            start = mid + 1
        mid = (start + end) // 2
    return mid

def coordinateCompression(coordinates):
    compressionChart = sorted(list(set(coordinates)))
    compressedCoordinates = []
    for coordinate in coordinates:
        compressedCoordinates.append(binarySearch(compressionChart, coordinate))
    return compressionChart, compressedCoordinates

def cumulateSum(compressionChart, compressedCoordinates):
    prefixSum = []
    for _ in range(len(compressionChart)):
        prefixSum.append(0)

    i = len(compressedCoordinates) - 1
    cumulSum = 0
    while i >= 0:
        cumulSum += 1
        prefixSum[compressedCoordinates[i]] = cumulSum
        i -= 1
    return prefixSum

front = []
for _ in range(N):
    front.append(int(input()))
front.sort()
frontChart, compressFront = coordinateCompression(front)

side = []
for _ in range(M):
    side.append(int(input()))
side.sort()
sideChart, compressSide = coordinateCompression(side)

if front[-1] == side[-1]:
    # min count part
    minCount = 0
    lastI = None
    lastJ = None
    i = 0
    j = 0
    while lastI != i or lastJ != j:
        frontBar = front[i]
        sideBar = side[j]
        lastI = i
        lastJ = j
        if frontBar < sideBar:
            minCount += frontBar
            if i < len(front) - 1:
                i += 1
        elif frontBar > sideBar:
            minCount += sideBar
            if j < len(side) - 1:
                j += 1
        else:
            minCount += frontBar
            if i < len(front) - 1:
                i += 1
            if j < len(side) - 1:
                j += 1

    print(minCount, end=" ")

    # max count part
    frontSum = cumulateSum(frontChart, compressFront)
    sideSum = cumulateSum(sideChart, compressSide)

    maxCount = 0
    lastI = None
    lastJ = None
    lastHighBar = 0
    i = 0
    j = 0
    while lastI != i or lastJ != j:
        frontBar = frontChart[i]
        sideBar = sideChart[j]
        frontCount = frontSum[i]
        sideCount = sideSum[j]
        lastI = i
        lastJ = j
        if frontBar < sideBar:
            maxCount += (frontBar-lastHighBar) * frontCount * sideCount
            lastHighBar = frontBar
            if i < len(frontSum) - 1:
                i += 1
        elif frontBar > sideBar:
            maxCount += (sideBar-lastHighBar) * frontCount * sideCount
            lastHighBar = sideBar
            if j < len(sideSum) - 1:
                j += 1
        else:
            if frontBar != 0:
                maxCount += (frontBar - lastHighBar) * frontCount * sideCount
            if i < len(frontSum) - 1:
                i += 1
            if j < len(sideSum) - 1:
                j += 1
            lastHighBar = frontBar

    print(maxCount)
else:
    print(-1)