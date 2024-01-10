from sys import stdin
from collections import deque
V, E = map(int, stdin.readline().split(" "))
K = int(stdin.readline())
# 먼저 인접 리스트의 형식으로 받아서 겹치는 경로에 대한 최솟값으로 만들어준다.
# 그러고 나서는 knapsack이랑 비슷한 접근인 것 같기도 한데, 확실한 건 DP 문제라는 사실이다. 그리고 여기에 더해 DFS 방식을 활용할 수 있을 것 같다는 생각이 들었다. 생각해보니까 인접 리스트 전처리가 필요없을지도 모르겠다는 생각이 들었다.
# 우선 내 힘으로 풀어보고자 하고 안되면 Dijkstra 알고리즘을 공부하고 풀어봐야겠다.
# 이 문제를 언젠가 풀겠노라한 지 벌써 1년이 지났다. 그 사이 나는 Dijkstra 알고리즘을 무려 2번이나 배웠다.

dists = []
adjList = []
colors = []
for _ in range(V):
    dists.append("INF")
    adjList.append([])
    colors.append(0)
for _ in range(E):
    u,v,w = map(int, stdin.readline().split(" "))
    adjList[u-1].append((v-1,w))

def dijkstra(adjList, start):
    dists[start] = 0
    colors[start] = 2
    waiting = deque([start])
    while waiting:
        now = waiting.popleft()
        colors[now] = 2
        for vertex, time in adjList[now]:
            if colors[vertex] == 0:
                waiting.append(vertex)
                colors[vertex] = 1
            pathDist = dists[now] + time
            if dists[vertex] == "INF" or pathDist < dists[vertex]:
                dists[vertex] = pathDist

dijkstra(adjList, K-1)

for dist in dists:
    print(dist)