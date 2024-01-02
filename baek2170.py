N = int(input())

lines = []
for _ in range(N):
    lines.append(tuple(map(int, input().split(" "))))
lines.sort(key = lambda x:x[0])

totalLength = 0
endPoint = None
for line in lines:
    if endPoint is None:
        totalLength = line[1] - line[0]
        endPoint = line[1]
    elif endPoint < line[1]:
        if endPoint < line[0]:
            totalLength += line[1] - line[0]
        else:
            totalLength += line[1] - endPoint
        endPoint = line[1]

print(totalLength)