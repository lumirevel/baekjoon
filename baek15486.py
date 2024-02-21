from sys import stdin
N = int(stdin.readline())
TP = []
for i in range(N):
    Ti, Pi = map(int, stdin.readline().split(" "))
    TP.append((i, i+Ti-1, Pi))


# DP[i]는 i+1에 퇴사할 때의 최대 값. 즉, i+1부터 회의 잡기 가능
TP.sort(key=lambda x:x[1])
beforeEnd = None
DP = [0] * N
for begin, end, P in TP:
    if beforeEnd is not None:
        for i in range(beforeEnd, min(N, end)-1):
            DP[i+1] = max(DP[i+1], DP[i])
    beforeEnd = end
    if end < len(DP):
        if begin == 0:
            DP[end] = max(DP[end], P)
        else:
            DP[end] = max(DP[end], DP[begin-1] + P)


print(DP[-1])
