# from sys import stdin
# N =int(stdin.readline())
# L = []
# for _ in range(N):
#     L.append(int(stdin.readline()))
# rst = sorted(L)
# for i in rst:
#     print(i)

from sys import stdin
N =int(stdin.readline())
L = dict()
for _ in range(N):
    k = int(stdin.readline())
    if k in L:
        L[k] += 1
    else:
        L[k] = 1

for key in sorted(L.keys()):
    for _ in range(L[key]):
        print(key)
