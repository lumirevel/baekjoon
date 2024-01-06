N = int(input())
superiorOf = list(map(int, input().split(" ")))

inferiorsOf = []
for _ in range(N):
    inferiorsOf.append([])
for i in range(N):
    if superiorOf[i] != -1:
        inferiorsOf[superiorOf[i]].append(i)

count = []
for _ in range(N):
    count.append(0)
def countDFS(inferiors, node=0):
    count[node] += len(inferiors[node])
    for inferior in inferiors[node]:
        count[node] += countDFS(inferiors, inferior)
    return count[node]


def timeDFS(inferiors, node=0, time=0):
    inferiors[node].sort(key=lambda x: count[x], reverse=True)

    totalTime = time
    for inferior in inferiors[node]:
        time += 1
        totalTime = max(totalTime, timeDFS(inferiors, inferior, time))
    return totalTime

countDFS(inferiorsOf)
print(timeDFS(inferiorsOf))
