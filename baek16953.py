A, B = map(int, input().split(" "))

def make(A, B, depth = 1):
    if A == B:
        return depth
    elif A > B:
        return -1
    else:
        newDepth = -1
        if B % 10 == 1:
            newDepth = make(A, B//10, depth+1)
        if B % 2 == 0:
            newDepth = make(A, B//2, depth+1)
        return newDepth

print(make(A, B))