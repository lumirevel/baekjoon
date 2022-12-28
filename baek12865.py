from sys import stdin

N, K = map(int, stdin.readline().split(" "))

DP = dict()

for n in range(1, N+1):
    W, V = map(int, stdin.readline().split(" "))
    DP[n] = dict()
    if n == 1:
        for w in range(K+1):
            if w < W:
                DP[n][w] = 0
            else:
                DP[n][w] = V
    else:
        for w in range(K+1):
            if w < W:
                DP[n][w] = DP[n-1][w]
            else:
                DP[n][w] = max(DP[n-1][w], DP[n-1][w-W] + V)

print(DP[N][K])

# [maxW, sumV, occupied]

# weight를 기준으로 sort하면 큰 weight가 먼저 들어가는 문제가 발생할 수 있음
# local maximum에서 벗어나는 방법을 찾아야 하는 것이다.
# tree를 그려볼까?
# 정해진 weight에 대한 value tree?
# 아 저장을 weight와 value를 합친 값으로 뭉쳐서 한다면?
# DP방식으로 weight value 조합을 여러 개 만들어 저장하고 weight
# DP[weight] = value