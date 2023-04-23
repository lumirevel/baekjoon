from sys import stdin

N = int(stdin.readline())

class Matrix(tuple):
    def __new__(cls, i,j):
        cache = [[None for _ in range(j)] for _ in range(i)]
        return tuple.__new__(cls, cache)

    def set(self, x):
        for i in range(len(x)):
            for j in range(len(x[0])):
                self[i][j] = x[i][j]

    def __mul__(self, other):
        p = 1000000007
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
        return M
    else:
        cache = powMat(n//2, M)
        if n % 2 == 0:
            return cache * cache
        else:
            return cache * cache * M

M = Matrix(2,2)
M.set(((1,1),(1,0)))
if N == 1:
    print(1)
else:
    print((powMat(N-1, M) * [[1],[0]])[0][0])