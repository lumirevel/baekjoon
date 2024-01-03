N = int(input())
scoreMap = []
for _ in range(N):
    scoreMap.append(tuple(map(int, input().split(" "))))

minDP = [0, 0, 0]
maxDP = [0, 0, 0]
for scoreLine in scoreMap:
    minx, miny, minz = minDP
    maxx, maxy, maxz = maxDP
    x, y, z = scoreLine
    minDP = [x + min(minx, miny), y + min(minx, miny, minz), z + min(miny, minz)]
    maxDP = [x + max(maxx, maxy), y + max(maxx, maxy, maxz), z + max(maxy, maxz)]
print(f"{max(maxDP)} {min(minDP)}")