N, M = map(int, input().split(" "))

front = []
for _ in range(N):
    front.append(int(input()))
front.sort()
frontChart = sorted(list(set(front)))
compressFront = []
for bar in front:
    start = 0
    end = len(frontChart) - 1
    mid = (start + end) // 2
    while frontChart[mid] != bar:
        now = frontChart[mid]
        if bar < now:
            end = mid-1
        elif bar > now:
            start = mid+1
        mid = (start + end) // 2
    compressFront.append(mid)

side = []
for _ in range(M):
    side.append(int(input()))
side.sort()
sideChart = sorted(list(set(side)))
compressSide = []
for bar in side:
    start = 0
    end = len(sideChart) - 1
    mid = (start + end) // 2
    while sideChart[mid] != bar:
        now = sideChart[mid]
        if bar < now:
            end = mid-1
        elif bar > now:
            start = mid+1
        mid = (start + end) // 2
    compressSide.append(mid)

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

    print(minCount)

    # max count part
    frontSum = []
    for _ in range(len(frontChart)):
        frontSum.append(0)
    i = len(frontChart) - 1
    cumulSum = 0
    while i >= 0:
        cumulSum += 1
        frontSum[compressFront[i]] = cumulSum
        i -= 1

    sideSum = []
    for _ in range(len(sideChart)):
        sideSum.append(0)
    j = len(sideChart) - 1
    cumulSum = 0
    while j >= 0:
        cumulSum += 1
        sideSum[compressSide[j]] = cumulSum
        j -= 1

    maxCount = 0
    lastI = None
    lastJ = None
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
            maxCount += (frontBar-frontChart[i]+1) * frontCount * sideCount
            if i < len(frontSum) - 1:
                i += 1
        elif frontBar > sideBar:
            maxCount += (sideBar-sideChart[j]+1) * frontCount * sideCount
            if j < len(sideSum) - 1:
                j += 1
        else:
            maxCount += frontCount * sideCount
            if i < len(frontSum) - 1:
                i += 1

            if j < len(sideSum) - 1:
                j += 1

    print(maxCount)
else:
    print(-1)