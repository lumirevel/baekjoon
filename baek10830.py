from sys import stdin

N, B = map(int,stdin.readline().split(" "))
input_list = list()
for _ in range(N):
    input_list.append(list(map(int, stdin.readline().split(" "))))

class Matrix(tuple):
    def __new__(cls, i,j):
        cache = [[None for _ in range(j)] for _ in range(i)]
        return tuple.__new__(cls, cache)

    def set(self, x):
        for i in range(len(x)):
            for j in range(len(x[0])):
                self[i][j] = x[i][j]

    def __mul__(self, other):
        p = 1000
        m, n, l = len(self), len(self[0]), len(other[0])
        c = Matrix(m,n)
        for i in range(m):
            for k in range(l):
                c[i][k] = 0
                for j in range(n):
                    c[i][k] += (self[i][j]*other[j][k]) % p
                c[i][k] %= p
        return c

def powMat(n, M):
    if n == 1:
        I = Matrix(N,N)
        cache = []
        for i in range(N):
            cache_x = []
            for j in range(N):
                cache_x.append(int(i==j))
            cache.append(cache_x)
        I.set(cache)
        return M * I
    else:
        cache = powMat(n//2, M)
        if n % 2 == 0:
            return cache * cache
        else:
            return cache * cache * M

M = Matrix(N,N)
M.set(input_list)
result = powMat(B, M)
for lst in result:
    for element in lst:
        print(element, end=" ")
    print()