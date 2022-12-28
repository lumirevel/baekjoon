# 성호 형의 약간의 도 pow함수의 횟수를 줄여줌
from sys import stdin
N, K = map(int, stdin.readline().rstrip().split(" "))
p = 1000000007

def pow(a, t, p):
    if t == 0:
        return 1
    elif t == 1:
        return a % p
    else:
        cache = pow(a, t//2, p)
        return (cache * cache * a ** (t % 2)) % p

up = 1
for i in range(K+1, N+1):
    up *= (i % p)
    up %= p

down = 1
for i in range(1, N-K+1):
    down *= i % p
    down %= p

down = pow(down, p-2, p)

rst = (up * down) % p

print(rst)