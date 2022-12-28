from sys import stdin
N = int(stdin.readline())

class Heap:
    def __init__(self):
        self.n = 0
        self.tree = [0]
    def append(self, a):
        self.n += 1
        2*n, 2*n+1

    def pop(self):
        if self.n:
            pass
        else:
            return 0

heap = Heap()

for _ in range(N):
    x = int(stdin.readline())
    if x > 0 :
        heap.append(x)
    else:
        print(heap.pop())