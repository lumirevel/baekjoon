N = int(input())
adjList = []
for _ in range(N):
    adjList.append([])
for _ in range(N-1):
    parent, child, length = map(int, input().split(" "))
    adjList[parent-1].append((child-1, length))
    adjList[child-1].append((parent-1, length))

def farthestFind(adjList, visited, now = 0, totalLength = 0):
    farthestChild = now
    farthestLength = totalLength
    for childInfo in adjList[now]:
        child, length = childInfo
        if not visited[child]:
            visited[child] = True
            farChild, farLength = farthestFind(adjList, visited, child, totalLength+length)
            if farthestLength < farLength:
                farthestLength = farLength
                farthestChild = farChild
    return farthestChild, farthestLength

firstFarChild, length = farthestFind(adjList, [False] * N)
secondFarChild, treeRadius = farthestFind(adjList, [False] * N, firstFarChild)
print(treeRadius)
