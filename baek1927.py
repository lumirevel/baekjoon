from sys import stdin
N = int(stdin.readline())

class Heap:
    def __init__(self):
        self.__N = 0
        self.tree = [None]
    def append(self, a):
        self.__N += 1
        if self.__N < len(self.tree):
            self.tree[self.__N] = a
        else:
            self.tree.append(a)

        p = self.__N // 2
        i = self.__N
        while p != 0 and self.tree[p] > self.tree[i]:
            self.tree[p], self.tree[i] = self.tree[i], self.tree[p]
            i = p
            p //= 2

    def pop(self):#is not implemented completely
        if self.__N:
            i = 1
            m = self.tree[i]

            self.tree[self.__N], self.tree[1] = self.tree[1], self.tree[self.__N]
            self.__N -= 1
            self.tree.pop()

            self.__bubble(1)

            return m
        else:
            return 0

    def __bubble(self, focus):
        l, r = 2*focus, 2*focus+1
        if r <= self.__N:
            if self.tree[l] < self.tree[focus]:
                if self.tree[l] < self.tree[r]:
                    self.tree[l], self.tree[focus] = self.tree[focus], self.tree[l]
                    self.__bubble(l)
                else:
                    self.tree[r], self.tree[focus] = self.tree[focus], self.tree[r]
                    self.__bubble(r)
            elif self.tree[r] < self.tree[focus]:
                self.tree[r], self.tree[focus] = self.tree[focus], self.tree[r]
                self.__bubble(r)
        elif l <= self.__N:
            if self.tree[l] < self.tree[focus]:
                self.tree[l], self.tree[focus] = self.tree[focus], self.tree[l]

    def __len__(self):
        return self.__N

heap = Heap()

for _ in range(N):
    x = int(stdin.readline())
    if x > 0 :
        heap.append(x)
    else:
        print(heap.pop())