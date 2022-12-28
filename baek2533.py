from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
N = int(stdin.readline())

tree = dict()
for _ in range(N):
    u, v = map(int, stdin.readline().rstrip().split(" "))
    if u in tree.keys():
        tree[u].append(v)
    else:
        tree[u] = [v]
    if u in tree.keys():
        tree[v].append(u)
    else:
        tree[v] = [u]

adaptors = []

def DFS():
    pass