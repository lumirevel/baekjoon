from sys import stdin
c = int(stdin.readline())

for _ in range(c):
    d, n = map(int, stdin.readline().split(" "))
    numList = list(map(int, stdin.readline().split(" ")))

    remainder = [0] * d
    nowRemain = 0
    count = 0
    for num in numList:
        remainder[nowRemain] += 1
        nowRemain -= num % d
        nowRemain %= d
        count += remainder[nowRemain]
    print(count)