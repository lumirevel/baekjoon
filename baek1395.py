from sys import stdin
N, M = map(int,input().split(" "))

class ToggleTree:
    def __init__(self, N):
        self.tree = [None]
        self.leafI = 1
        while self.leafI < N:
            self.leafI *= 2
        for _ in range(2*self.leafI):
            self.tree.append(None)
        self.tree[1] = False

    def toggle(self, i, j, node = None, start = None, end = None, prev = None):
        # 가는 중에 대충 max 만날시 쪼개기 or 덮어쓰기
        # 쪼개기의 경우 밑으로 내려가면 무조건 덮어쓰기
        if node is None:
            node = 1
        if start is None:
            start = 0
        if end is None:
            end = self.leafI-1

        if i <= start and end <= j: # correct
            if prev is not None:
                self.tree[node] = not prev
            elif self.tree[node] is not None:
                self.tree[node] = not self.tree[node]
            else:
                mid = (start + end) // 2
                left = self.toggle(i, j, 2 * node, start, mid, None)
                right = self.toggle(i, j, 2 * node + 1, mid + 1, end, None)

                if left == right:
                    self.tree[node] = left
                    self.tree[2 * node] = None
                    self.tree[2 * node + 1] = None
        elif end < i or j < start:
            if prev is not None:
                self.tree[node] = prev
        else:
            if prev is not None:
                now = prev
            else:
                now = self.tree[node]
            self.tree[node] = None

            mid = (start+end) // 2
            left = self.toggle(i, j, 2*node, start, mid, now)
            right = self.toggle(i, j, 2*node+1, mid+1, end, now)

            if left == right:
                self.tree[node] = left
                self.tree[2*node] = None
                self.tree[2*node+1] = None
        return self.tree[node]

    def count(self, i, j):
        count = 0
        waitingList = [(1, 0, self.leafI - 1)]
        while waitingList:
            node, start, end = waitingList.pop()
            value = self.tree[node]
            if value is None:
                mid = (start + end) // 2
                waitingList.append((2 * node + 1, mid + 1, end))
                waitingList.append((2 * node, start, mid))
            elif value:
                if i <= start and end <= j or not (end < i or j < start):
                    count += min(j, end) - max(i, start) + 1
        return count

switches = ToggleTree(N)
for _ in range(M):
    O, S, T = map(int, stdin.readline().split(" "))
    if O == 0:
        switches.toggle(S-1,T-1)
    elif O == 1:
        print(switches.count(S-1,T-1))