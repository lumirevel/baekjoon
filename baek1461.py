N, M = map(int, input().split(" "))
bookPositions = list(map(int, input().split(" ")))
bookPositions.sort()

steps = 0

# negative
if bookPositions[0] < 0:
    i = 0
    while i < len(bookPositions) and bookPositions[i] < 0:
        steps += 2 * -bookPositions[i]
        i += M
    if bookPositions[-1] < 0 or -bookPositions[0] > bookPositions[-1]:
        steps -= -bookPositions[0]

# positive
if bookPositions[-1] > 0:
    i = len(bookPositions)-1
    while i >= 0 and bookPositions[i] > 0:
        steps += 2 * bookPositions[i]
        i -= M
    if bookPositions[0] > 0 or -bookPositions[0] < bookPositions[-1]:
        steps -= bookPositions[-1]

print(steps)