from sys import stdin
N = int(stdin.readline())
TPList = []
for _ in range(N):
    TPList.append([])
for i in range(N):
    Ti, Pi = map(int, stdin.readline().split(" "))
    end = i+Ti-1
    if end < len(TPList):
        TPList[end].append((i, Pi))


# DP[i]는 i+1에 퇴사할 때의 최대 값. 즉, i+1부터 회의 잡기 가능
DP = [0] * N
for i, counselList in enumerate(TPList):
    if i != 0:
        DP[i] = DP[i-1]
    for counsel in counselList:
        begin, P = counsel
        if begin == 0:
            DP[i] = max(DP[i], P)
        else:
            DP[i] = max(DP[i], DP[begin-1] + P)


print(DP[-1])
