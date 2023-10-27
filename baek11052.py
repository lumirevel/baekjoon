N = int(input())
P = [0] + list(map(int, input().split(" ")))

MaxPrice =[0,P[1]]
for i in range(2, N+1):
    maxPi = 0
    if (i<=N):maxPi = P[i]
    for j in range(1, i):
        maxPi = max(maxPi, MaxPrice[j] + MaxPrice[i-j])
    MaxPrice.append(maxPi)

print(MaxPrice.pop())