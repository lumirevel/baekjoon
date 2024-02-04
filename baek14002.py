N = int(input())
numList = list(map(int, input().split(" ")))

maxIndex = 0
maxCount = 1
DP = [1] * len(numList)
for i in range(len(numList)-1):
    for j in range(i+1, len(numList)):
        if numList[i] < numList[j] and DP[j] < DP[i]+1:
            DP[j] = DP[i]+1
            if maxCount < DP[j]:
                maxCount = DP[j]
                maxIndex = j

print(maxCount)

sequence = []
for j in range(maxIndex, -1, -1):
    if DP[j] == maxCount:
        sequence.append(numList[j])
        maxCount -= 1

while sequence:
    print(sequence.pop(), end=' ')
