from sys import stdin
N = int(stdin.readline())
meeting = []
for _ in range(N):
    meeting.append(tuple(map(int, stdin.readline().split(" "))))
meeting.sort(key=lambda x:x[1])

DP = []


def P(j):
    i = j - 1
    while i != -1 and meeting[i][1] > meeting[j][0]:
        i -= 1
    if i < 0:
        return None
    else:
        return i


for j, meet in enumerate(meeting):
    if j == 0:
        DP.append(meet[2])
    else:
        i = P(j)
        if i is not None:
            DP.append(max(DP[j - 1], DP[i] + meet[2]))
        else:
            DP.append(max(DP[j - 1], meet[2]))

print(DP[-1])
