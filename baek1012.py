from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
T = int(stdin.readline())
tree = []
visited = []
def dfs(i):
    visited[i] = True
    for node in tree[i]:
        if not visited[node]:
            dfs(node)

for _ in range(T):
    M, N, K = map(int, stdin.readline().rstrip().split(" "))
    field = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(K):
        X, Y = map(int, stdin.readline().rstrip().split(" "))
        field[X][Y] = i+1
    tree = [[] for _ in range(K+1)]
    visited = [False for _ in range(K+1)]
    for i in range(M):
        for j in range(N):
            if field[i][j]:
                if i != 0:
                    if field[i-1][j]:
                        tree[field[i-1][j]].append(field[i][j])
                        tree[field[i][j]].append(field[i-1][j])
                if i != M-1:
                    if field[i+1][j]:
                        tree[field[i+1][j]].append(field[i][j])
                        tree[field[i][j]].append(field[i+1][j])
                if j != 0:
                    if field[i][j-1]:
                        tree[field[i][j-1]].append(field[i][j])
                        tree[field[i][j]].append(field[i][j-1])
                if j != N-1:
                    if field[i][j+1]:
                        tree[field[i][j+1]].append(field[i][j])
                        tree[field[i][j]].append(field[i][j+1])
    count = 0
    for i in range(K):
        if not visited[i+1]:
            count += 1
            dfs(i+1)
    print(count)