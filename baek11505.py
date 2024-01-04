from sys import stdin

class SegTree:
    def __init__(self, n):
        self.tree = [None]
        self.leafI = 1
        while self.leafI < n:
            self.leafI *= 2
        for _ in range(2*self.leafI):
            self.tree.append(1)

    def nodeRange(self, index):
        lgI = 0
        t = 1
        while 2*t <= index:
            lgI += 1
            t *= 2
        bs = self.leafI/t
        offset = index - t
        return (bs*offset, bs-1+bs*offset)

    def nodeMiddle(self, s, e):
        return s+(e-s)/2

    def update(self, i, v):
        index = self.leafI + i
        self.tree[index] = v % 1000000007
        index //= 2
        while index > 0:
            self.tree[index] = self.tree[2*index]*self.tree[2*index+1] % 1000000007
            index //= 2

    def line(self, s, e):
        mul = 1
        nowNodeIndex = [1, 1]
        startFound = False
        endFound = False
        while not startFound or not endFound:
            if nowNodeIndex[0] == nowNodeIndex[1]:
                rng = self.nodeRange(nowNodeIndex[0])
                mid = self.nodeMiddle(*rng)
                if e < mid:
                    nowNodeIndex[0] = nowNodeIndex[1] = 2*nowNodeIndex[0]
                elif s > mid:
                    nowNodeIndex[0] = nowNodeIndex[1] = 2*nowNodeIndex[0]+1
                else:
                    if s != rng[0] or s != rng[1]:
                        nowNodeIndex[0] = 2 * nowNodeIndex[0]
                        nowNodeIndex[1] = 2 * nowNodeIndex[1] + 1
                    else:
                        mul = self.tree[nowNodeIndex[0]]
                        startFound = True
                        endFound = True
            else:
                if not startFound:
                    rngS = self.nodeRange(nowNodeIndex[0])
                    midS = self.nodeMiddle(*rngS)
                    if s == rngS[0] or 2*nowNodeIndex[0] > 2*self.leafI-1:
                        mul *= self.tree[nowNodeIndex[0]]
                        mul %= 1000000007
                        startFound = True
                    elif s < midS:
                        mul *= self.tree[2 * nowNodeIndex[0] + 1]
                        mul %= 1000000007
                        nowNodeIndex[0] = 2 * nowNodeIndex[0]
                    else:
                        nowNodeIndex[0] = 2 * nowNodeIndex[0] + 1

                if not endFound:
                    rngE = self.nodeRange(nowNodeIndex[1])
                    midE = self.nodeMiddle(*rngE)
                    if e == rngE[1] or 2*nowNodeIndex[1] > 2*self.leafI-1:
                        mul *= self.tree[nowNodeIndex[1]]
                        mul %= 1000000007
                        endFound = True
                    elif e < midE:
                        nowNodeIndex[1] = 2 * nowNodeIndex[1]
                    else:
                        mul *= self.tree[2 * nowNodeIndex[1]]
                        mul %= 1000000007
                        nowNodeIndex[1] = 2 * nowNodeIndex[1] + 1
        return mul



N,M,K = map(int, input().split(" "))

tree = SegTree(N)
for i in range(N):
    tree.update(i, int(stdin.readline()))
commands = []
for _ in range(M+K):
    commands.append(tuple(map(int, input().split(" "))))

for command in commands:
    if command[0] == 1:
        tree.update(command[1]-1, command[2])
    elif command[0] == 2:
        print(tree.line(command[1]-1, command[2]-1))
