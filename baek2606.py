from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, stdin.readline().rstrip().split(" "))
    tree[i].append(j)
    tree[j].append(i)

visited = [False for _ in range(N+1)]
count = -1
def dfs(i):
    visited[i] = True
    global count
    count += 1
    for node in tree[i]:
        if not visited[node]:
            dfs(node)

dfs(1)
print(count)