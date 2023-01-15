from sys import stdin
N = int(stdin.readline())

class Meet:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w
        self.i = None
    def __repr__(self):
        return f"{self.s} {self.e} {self.w}"


meeting = []
for _ in range(N):
    s, e, w = map(int, stdin.readline().split(" "))
    meeting.append(Meet(s,e,w))
meeting.sort(key=lambda x:x.e)

sort_by_start_meeting = []
for i, v in enumerate(meeting):
    v.i = i
    sort_by_start_meeting.append(v)
sort_by_start_meeting.sort(key=lambda x:x.s)

P = [None for _ in range(N)]
i, j = N - 1, N - 1
while j >= 0:
    while i != 0 and meeting[i].e > sort_by_start_meeting[j].s:
        i -= 1
    if meeting[i].e <= sort_by_start_meeting[j].s:
        P[sort_by_start_meeting[j].i] = i
    j -= 1

DP = []
for j, meet in enumerate(meeting):
    if j == 0:
        DP.append(meet.w)
    else:
        i = P[j]
        if i is not None:
            DP.append(max(DP[j - 1], DP[i] + meet.w))
        else:
            DP.append(max(DP[j - 1], meet.w))

print(DP[-1])
