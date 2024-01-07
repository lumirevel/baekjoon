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
def subTreeLengths(adj, node=0):
    visited[node] = True
    # 까지의 최대 거리와 subtree에서의 maxLength 둘 다 출격
    subMaximum = 0

    toMaximum = 0
    toSecondMaximum = None
    for toNode, w in adj[node]:
        if not visited[toNode]:
            toMax, subMax = subTreeLengths(adj, toNode)
            if subMaximum is None or subMaximum < subMax:
                subMaximum = subMax
            if toMaximum is None or toMaximum < toMax + w:
                toSecondMaximum = toMaximum
                toMaximum = toMax + w
    if toMaximum is None:
        return (toMaximum, subMaximum)
    elif toSecondMaximum is None:
        return (toMaximum, max(subMaximum, toMaximum))
    else:
        return (toMaximum, max(subMaximum, toMaximum + toSecondMaximum))

trash, result = subTreeLengths(adj)
print(result)