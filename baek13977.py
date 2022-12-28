# from sys import stdin
# p = 1000000007
#
# def pow(a, t, p):
#     if t == 0:
#         return 1
#     elif t == 1:
#         return a % p
#     else:
#         cache = pow(a, t // 2, p)
#         return (cache * cache * a ** (t % 2)) % p
#
# M = int(stdin.readline())
#
# for _ in range(M):
#     N, K = map(int, stdin.readline().split(" "))
#
#     up = 1
#     down = 1
#     if K+1 < N-K+1:
#         for i in range(1, K + 1):
#             up *= (N + 1 - i) % p
#             up %= p
#
#             down *= i % p
#             down %= p
#     else:
#         for i in range(1, N - K + 1):
#             up *= (K + i) % p
#             up %= p
#
#             down *= i % p
#             down %= p
#
#     rst = (up * pow(down, p - 2, p)) % p
#     print(rst)

from sys import stdin
p = 1000000007

factorial = [1]
for i in range(4000000):
    factorial.append(((i+1) * factorial[i]) % p)

def pow(a, t, p):
    if t == 0:
        return 1
    elif t == 1:
        return a % p
    else:
        cache = pow(a, t // 2, p)
        return (cache * cache * a ** (t % 2)) % p

M = int(stdin.readline())

for _ in range(M):
    N, K = map(int, stdin.readline().split(" "))

    rst = (factorial[N] * pow((factorial[N-K]*factorial[K]) % p, p - 2, p)) % p
    print(rst)