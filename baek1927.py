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
            m = self.tree[1]
            i = 1
            while 2*i < self.__N:
                if self.tree[2*i] < self.tree[2*i+1]:
                    self.tree[i], self.tree[2*i] = self.tree[2*i], self.tree[i]
                    i = 2*i
                else:
                    self.tree[i], self.tree[2 * i + 1] = self.tree[2 * i + 1], self.tree[i]
                    i = 2*i+1

            if self.__N <= 2 * i:
                self.tree[i], self.tree[2 * i] = self.tree[2 * i], self.tree[i]
            elif self.__N <= 2*i+1:
                if self.tree[2 * i] < self.tree[2 * i + 1]:
                    self.tree[i], self.tree[2 * i] = self.tree[2 * i], self.tree[i]
                    self.tree[2*i], self.tree[2*i+1] = self.tree[2*i+1], self.tree[2*i]
                else:
                    self.tree[i], self.tree[2 * i + 1] = self.tree[2 * i + 1], self.tree[i]
            self.tree.pop()
            self.__N -= 1
            return m
        else:
            return 0

    def __len__(self):
        return self.__N

heap = Heap()

for _ in range(N):
    x = int(stdin.readline())
    if x > 0 :
        heap.append(x)
    else:
        print(heap.pop())

print(heap.tree[1])