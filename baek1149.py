N = int(input())

costList = []
for _ in range(N):
    costList.append(list(map(int, input().split(" "))))

R = 0
G = 1
B = 2

DP = [0] * 3
for cost in costList:
    redDP = DP[R]
    greenDP = DP[G]
    blueDP = DP[B]

    DP[R] = min(greenDP, blueDP) + cost[R]
    DP[G] = min(redDP, blueDP) + cost[G]
    DP[B] = min(redDP, greenDP) + cost[B]

print(min(DP))