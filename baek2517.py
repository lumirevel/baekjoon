class SegTree:
    def __init__(self, n):
        self.tree = [None]
        self.leafD = 0
        self.leafI = 1
        while n > self.leafI:
            self.leafI *= 2
            self.leafD += 1
        for _ in range(2*self.leafI):
            self.tree.append(0)

    def addAt(self, v):
        i = self.leafI + v
        while i > 0:
            self.tree[i] += 1
            i //= 2

    def sumUntil(self, k):
        sum = 0
        t = 1
        s = 0
        e = self.leafI-1
        while k != e:
            if k < s+(e-s)/2:
                t = self.left(t)
                e = s + (e - s) // 2
            else:
                sum += self.tree[self.left(t)]
                t = self.right(t)
                s = s+(e-s)//2+1
        sum += self.tree[t]
        return sum

    def left(self, k):
        return 2*k

    def right(self, k):
        return 2*k+1

N = int(input())

abilities = []
for _ in range(N):
    abilities.append(int(input()))
newbilities = abilities.copy()
newbilities.sort()
zipbilities = []
for ability in abilities:
    start = 0
    end = N
    i = N//2
    while newbilities[i] != ability:
        if ability < newbilities[i]:
            end = i
            i = start + (i - start) // 2
        else:
            start = i
            i = end - (end - i) // 2
    zipbilities.append(i)

tree = SegTree(N)
for i,zipbility in enumerate(zipbilities):
    print(i-tree.sumUntil(zipbility)+1)
    tree.addAt(zipbility)