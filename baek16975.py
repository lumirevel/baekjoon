from sys import stdin

class QueryTree:
    def __init__(self,lst):
        n = len(lst)
        self.tree = [None]
        self.leafI = 1
        while self.leafI < n:
            self.leafI *= 2
        for i in range(1,2*self.leafI):
            if i < self.leafI:
                self.tree.append(0)
            elif i < self.leafI + n:
                self.tree.append(lst[i-self.leafI])
            else:
                self.tree.append(None)
    def query(self,i,j,k):
        waitingList = [(1, 0, self.leafI-1)]
        while waitingList:
            node, nodeStart, nodeEnd = waitingList.pop()
            if i <= nodeStart and nodeEnd <= j:
                self.tree[node] += k
            elif nodeEnd < i or j < nodeStart:
                pass
            else:
                mid = (nodeStart + nodeEnd) // 2
                waitingList.append((2*node, nodeStart, mid))
                waitingList.append((2*node+1, mid+1, nodeEnd))
    def check(self, x):
        node = 1
        start = 0
        end = self.leafI - 1
        cumul = 0
        while start != end:
            cumul += self.tree[node]
            mid = (start + end) // 2
            if x <= mid:
                node = 2*node
                end = mid
            else:
                node =2*node+1
                start = mid+1
        return  cumul+self.tree[node]

N = int(input())
tree = QueryTree(list(map(int, stdin.readline().split(" "))))

M = int(input())
for _ in range(M):
    query = list(map(int, stdin.readline().split(" ")))
    if query[0] == 1:
        i,j,k = query[1:]
        tree.query(i-1,j-1,k)
    elif query[0] == 2:
        print(tree.check(query[1]-1))