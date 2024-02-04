N = int(input())

if ((N+1)//2) % 2 == 1:
    print(0)
else:
    sum1N = (N*(N+1))//2
    DP = [0] * sum1N
    for n in range(N):
        for i in range(sum1N-1, n, -1):
            DP[i] += DP[i-n-1]
        DP[n] += 1
    print((DP[(N*(N+1))//4-1]+1)//2)
