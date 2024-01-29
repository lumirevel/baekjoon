N = int(input())

primeList = []
for num in range(1, N+1):
    if num == 1:
        print(1, end=" ")
    else:
        isPrime = True
        i = 0
        while i < len(primeList) and isPrime and primeList[i]*primeList[i] <= num:
            if num % primeList[i] == 0:
                isPrime = False
                print(i+2, end=" ")
            i += 1
        if isPrime:
            primeList.append(num)
            print(len(primeList)+1, end=" ")
