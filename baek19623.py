from sys import stdin
N = int(stdin.readline())
meeting = []
for _ in range(N):
    meeting.append(tuple(map(int, stdin.readline().split(" "))))