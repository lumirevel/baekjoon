n = int(input())
numList = input().split(" ")

i = 0
while i < len(numList):
    j = 0
    while j < len(numList)-1 - i:
        if int(numList[j] + numList[j+1]) < int(numList[j+1] + numList[j]):
            numList[j], numList[j+1] = numList[j+1], numList[j]
        j += 1
    i += 1

print(int(str().join(numList)))