N = int(input())

maxColor = 1
primeList = []
coloredList = [1]
for num in range(2, N+1):
    isPrime = True
    i = 0
    while i < len(primeList) and isPrime and primeList[i]*primeList[i] <= num:
        if num % primeList[i] == 0:
            isPrime = False
            color = i+2
            maxColor = max(maxColor, color)
            coloredList.append(color)
        i += 1
    if isPrime:
        primeList.append(num)
        color = len(primeList)+1
        maxColor = max(maxColor, color)
        coloredList.append(color)

print(maxColor)
for color in coloredList:
    print(color, end=" ")
