N = int(input())
superiorOf = list(map(int, input().split(" ")))

inferiorsOf = []
for _ in range(N):
    inferiorsOf.append([])
for i in range(N):
    if superiorOf[i] != -1:
        inferiorsOf[superiorOf[i]].append(i)

times = []
for _ in range(N):
    times.append(0)
def timeDFS(inferiors, this=0):
    for inferior in inferiors[this]:
        timeDFS(inferiors, inferior)
    inferiors[this].sort(key = lambda x:times[x], reverse = True)

    for i, inferior in enumerate(inferiors[this]):
        times[this] = max(times[this], times[inferior]+i+1)

timeDFS(inferiorsOf)
print(times[0])
