N = int(input())
numList = list(map(int, input().split(" ")))

DP = [1] * len(numList)
for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        DP[j] = max(DP[j], DP[i]+(numList[i] < numList[j]), DP[j-1])

print(DP[-1])