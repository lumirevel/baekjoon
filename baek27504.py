from sys import stdin
N = int(stdin.readline())

musicList = []
for _ in range(N):
    musicList.append(list(map(int, stdin.readline().split(" "))))
L = int(stdin.readline())
b = list(map(int, stdin.readline().split(" ")))

melodyKey = []
for i in range(len(b)-1):
    melodyKey.append(b[i+1] - b[i])
duplicatedKeyList = [None] * (len(b)-1)
startPoint = None
for i, key in enumerate(melodyKey):
    if startPoint is None:
        if key == melodyKey[0]:
            startPoint = i
    elif key != melodyKey[i-startPoint]:
        duplicatedKeyList[i] = i-startPoint

foundedList = []
for i, music in enumerate(musicList):
    Ki = music[0]
    startPoint = None
    for j in range(1, len(music)-2):
        key = music[j+1] - music[j]
        if startPoint is None:
            if key == melodyKey[0]:
                startPoint = j
        elif key != melodyKey[j-startPoint]:
            candidatedNow = duplicatedKeyList[j-startPoint]
            if candidatedNow is None:
                startPoint = None
            else:
                if key == melodyKey[candidatedNow]:
                    startPoint = j - candidatedNow
                else:
                    startPoint = None
        elif j - startPoint == len(melodyKey)-1:
            foundedList.append(i+1)
            break

if foundedList:
    for num in foundedList:
        print(num, end=" ")
else:
    print(-1)
