N = int(input())
numList = list(map(int, input().split(" ")))

maxCount = 1
DP = [1] * len(numList)
for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        if numList[i] < numList[j]:
            DP[j] = max(DP[j], DP[i] + 1)
        maxCount = max(maxCount, DP[j])

print(maxCount)