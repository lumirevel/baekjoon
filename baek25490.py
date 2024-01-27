from sys import stdin
from queue import PriorityQueue
N = int(stdin.readline())
B = list(map(int, stdin.readline().split(" ")))

def maxRangeConquer(B, i, j):
    if i == j:
        return [(i,i,i)]
    elif j < i:
        return []
    else:
        maxIndex = i
        for nowIndex in range(i,j+1):
            if B[maxIndex] < B[nowIndex]:
                maxIndex = nowIndex
        return maxRangeConquer(B, i, maxIndex-1) + [(i, maxIndex, j)] + maxRangeConquer(B, maxIndex+1, j)

def minRangeConquer(B, i, j):
    if i == j:
        return [(i,i,i)]
    elif j < i:
        return []
    else:
        minIndex = i
        for nowIndex in range(i,j+1):
            if B[minIndex] > B[nowIndex]:
                minIndex = nowIndex
        return minRangeConquer(B, i, minIndex-1) + [(i, minIndex, j)] + minRangeConquer(B, minIndex+1, j)

START = 0
NEED = 1
END = 2
minRangeSorted = sorted(minRangeConquer(B, 0, N-1), reverse=True)
minTrayRangeHeap = PriorityQueue()

operand = 1000000007
totalScore = 0
for maxRange in maxRangeConquer(B, 0, N-1):
    while minRangeSorted and minRangeSorted[-1][START] <= maxRange[NEED]:
        item = minRangeSorted.pop()
        minTrayRangeHeap.put((item[END], item))
    while minTrayRangeHeap.queue and minTrayRangeHeap.queue[0][0] < maxRange[NEED]:
        minTrayRangeHeap.get()
    for end, minRange in minTrayRangeHeap.queue:
        if minRange[NEED] <= maxRange[END] and maxRange[START] <= minRange[NEED]:
            minNeed = min(minRange[NEED], maxRange[NEED])
            maxNeed = max(minRange[NEED], maxRange[NEED])

            maxStart = max(minRange[START], maxRange[START])
            minEnd = min(minRange[END], maxRange[END])

            count = ((minNeed - maxStart + 1) % operand) * ((minEnd - maxNeed + 1) % operand) % operand
            totalScore += (count * B[minRange[NEED]] * B[maxRange[NEED]]) % operand
            totalScore %= operand

print(totalScore)