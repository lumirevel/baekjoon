from sys import stdin
N = int(stdin.readline())
tree = [[] for _ in range(N)]
parents = map(int, stdin.readline().rstrip().split(" "))
root = None
for i, parent in enumerate(parents):
    if parent == -1:
        root = i
    else:
        tree[parent].append(i)
        tree[i].append(parent)

leapcount = 0
visited = [False for _ in range(N)]
def dfs(i):
    visited[i] = True
    leap = True
    for node in tree[i]:
        if not visited[node]:
            leap = False
            dfs(node)
    if leap:
        global leapcount
        leapcount += 1

deleted = int(stdin.readline())


# if deleted == root:
#     children = tree[deleted]
#     for i in tree[deleted]:
#         tree[i].pop(tree[i].index(deleted))
#     for node in children:
#         dfs(node)
if deleted != root:
    for i in tree[deleted]:
        tree[i].pop(tree[i].index(deleted))
    dfs(root)

print(leapcount)