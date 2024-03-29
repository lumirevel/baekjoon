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
pi = [0] * len(melodyKey)
matched = 0
for i in range(1, len(melodyKey)):
    key = melodyKey[i]
    if key == melodyKey[matched]:
        matched += 1
        pi[i] = matched
    else:
        while matched != 0 and key != melodyKey[pi[matched-1]]:
            matched = pi[matched-1]

foundedList = []
for i, music in enumerate(musicList):
    Ki = music[0]
    matched = 0
    for j in range(1, len(music)-1):
        key = music[j+1] - music[j]
        if key == melodyKey[matched]:
            matched += 1
            if matched == len(melodyKey):
                foundedList.append(i+1)
                break
        else:
            while matched != 0 and key != melodyKey[pi[matched-1]]:
                matched = pi[matched-1]

if foundedList:
    for num in foundedList:
        print(num, end=" ")
else:
    print(-1)
