from sys import stdin
from collections import deque

V = int(input())
visited = []
adj = []
for _ in range(V):
    visited.append(False)
    adj.append([])
for _ in range(V):
    say = deque(map(int, stdin.readline().split(" ")))
    node = say.popleft()
    toNode = say.popleft()
    while toNode != -1:
        w = say.popleft()
        adj[node-1].append((toNode-1, w))
        toNode = say.popleft()

# max와 max 직전
# subMaximum = subTreeLengths에 들어온 node를 root로 한 subtree의 지름
# toMaximum = subTreeLengths에 들어온 node를 root로 한 subtree의 leaf 노드에서 root 노드까지의 거리의 최댓값
def subTreeLengths(adj, node=0):
    visited[node] = True
    # 까지의 최대 거리와 subtree에서의 maxLength 둘 다 출력
    subMaximum = 0

    toMaximum = 0
    toSecondMaximum = None
    for toNode, w in adj[node]:
        if not visited[toNode]:
            toMax, subMax = subTreeLengths(adj, toNode)
            if subMaximum < subMax:
                subMaximum = subMax
            if toMaximum <= toMax + w:
                toSecondMaximum = toMaximum
                toMaximum = toMax + w
            elif toSecondMaximum <= toMax + w:
                toSecondMaximum = toMax + w
    if toSecondMaximum is None:
        return (toMaximum, max(subMaximum, toMaximum))
    else:
        return (toMaximum, max(subMaximum, toMaximum + toSecondMaximum))

trash, result = subTreeLengths(adj)
print(result)
