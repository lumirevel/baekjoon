from sys import stdin

N, K = map(int, input().split(" "))
activities = []
for _ in range(N):
    activities.append(map(int, stdin.readline().split(" ")))
rooms = []
for _ in range(K):
    rooms.append(0)

count = 0
for activity in activities:
    s, e = activity
    rooms.sort(reverse=True)
    i = 0
    while i < len(rooms):
        if rooms[i] < s:
            rooms[i] = e
            count += 1
            break
        i += 1

print(count)
