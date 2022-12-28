from sys import stdin
N, M, K = map(int, stdin.readline().split(" "))
array = []
for _ in range(N):
    array.append(int(stdin.readline()))

n = 0
cache = 1
while cache <= N:
    n += 1
    cache *= 2

segmentTree = [None for _ in range(2**(n+1)-2)]

def segmenting(i,j,d):
    if i == j:
        segmentTree[d] = array[i]
        return segmentTree[d]
    else:
        m = (i+j)//2
        segmentTree[d] = segmenting(i, m, 2*d+1) + segmenting(m+1, j, 2*d+2)
        return segmentTree[d]

def modifying(a,b,i,v,d):
    m = (a+b)//2
    if a == b:
        cache = segmentTree[d]
        segmentTree[d] = v
        return segmentTree[d] - cache
    elif a <= i <= m:
        modified = modifying(a, m, i, v, 2*d+1)
        segmentTree[d] += modified
        return modified
    elif m+1 <= i <= b:
        modified = modifying(m+1, b, i, v, 2*d+2)
        segmentTree[d] += modified
        return modified

def sum(a,b,i,j,d):
    m = (a+b)//2
    S = 0
    if i <= a and b <= j:
        S += segmentTree[d]
    elif a != b:
        if not j < a and not b < i:
            S += sum(a, m, i, j, 2 * d + 1)
            S += sum(m + 1, b, i, j, 2 * d + 2)
    return S

segmenting(0, N-1, 0)

for _ in range(M+K):
    a, b, c = map(int, stdin.readline().split(" "))
    if a == 1:
        array[b-1] = c
        modifying(0, N-1, b-1, c, 0)
    elif a == 2:
        print(sum(0, N-1, b-1, c-1, 0))
