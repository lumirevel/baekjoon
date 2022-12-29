from sys import stdin
N, M = map(int, stdin.readline().split(" "))
m = [None] + list(map(int, stdin.readline().split(" ")))
c = [None] + list(map(int, stdin.readline().split(" ")))

"""
그냥 배낭 문제와는 다르다
배낭 문제는 채울 수 있는 채우는 것이므로 꼭 꽉 채울 필요가 없다
하지만 이 문제는 꼭 M의 메모리를 채워야 한다
즉 m값이 아닌 i번째로 많이 차지한 메모리 값으로 DP를 돌려야 한다는 말이다
즉 가중치 있는 회의실 문제처럼 풀면 된다는 소리다
아니 m보다 큰 메모리를 차지하는 조합 중 비용이 최소가 되는 것 중 가장 적은 메모리를 차지하는 경우를 찾으면 되나?
정확히 조건은 m보다 큰 메모리를 차지하는 조합 중 비용이 최소가 되는 것의 비용 값이 맞다
이렇게 되면 DP를 할 때 저장해야 하는 것은 이산적인 순서와 비용값이 되어야 하는 걸까?
그냥 n번째 단계에서는 n개까지 다 넣은 경우를 구하고 비교하면 될 듯?
그럼 층은 왜 지지?
회의실 문제랑 비슷한 개념인 게 맞는 지도?
아 회의실은 2차원 배열이 아닌 1차원 배열이었다
이것도 1차원 배열일 것 같다
근데 sorting이 필요할지도? ordered가 잘 되어 있어야 할 것 같은데? (well-ordered set?)
그 배낭문제를 뒤집으면 됨 - 메모리가 터짐
go and back 전략을 쓴다면?
지나간 곳을 참조하지 않기 때문에 1차원 배열로 축소 성공.
DP는 말 그대로 저장만 잘하면 되는 거였음.
꼭 점화식의 끝자락이 결과값일 필요가 없음.
N*m 대신 N*c 하니까 되었음
"""

DP = [[None for _ in range(100*N+1)] for _ in range(N+1)]
for n in range(1, N+1):
    if n == 1:
        for cstep in range(100*N+1):
            if cstep < c[n]:
                DP[n][cstep] = 0
            else:
                DP[n][cstep] = m[n]
    else:
        for cstep in range(100*N+1):
            if cstep < c[n]:
                DP[n][cstep] = DP[n-1][cstep]
            else:
                DP[n][cstep] = max(DP[n-1][cstep], DP[n-1][cstep-c[n]]+m[n])

cstep = 0
while DP[N][cstep] < M:
    cstep += 1

print(cstep)