# from sys import stdin, setrecursionlimit
# setrecursionlimit(1000)
# p = 1000000007
# T = int(stdin.readline())
#
# def parenthesis(N):
#     if N == 1:
#         return 0
#     elif N == 2:
#         return 1
#     else:
#         sum = 0
#         if N % 2 == 0:
#             for i in range(1, N//2+1):
#                 sum += (parenthesis(i)*parenthesis(N-i)) % p
#             return 2*sum % p
#         elif N % 2 == 1:
#             for i in range(1, N//2+1):
#                 sum += (parenthesis(i)*parenthesis(N-i)) % p
#             return (2*sum+parenthesis(N//2)**2) % p
#
# for _ in range(T):
#     print(parenthesis(int(stdin.readline())))

# from sys import stdin, setrecursionlimit
# setrecursionlimit(1000)
# p = 1000000007
# T = int(stdin.readline())
#
# DP = [None, 0, 1]
# def parenthesis(N):
#     for n in range(3, N+1):
#         sum = 0
#         if n % 2 == 0:
#             for i in range(1, n // 2 + 1):
#                 sum += (DP[i] * DP[n - i]) % p
#             DP.append(2 * sum % p)
#         elif n % 2 == 1:
#             for i in range(1, n // 2 + 1):
#                 sum += (DP[i] * DP[n - i]) % p
#             DP.append((2 * sum + DP[n // 2] ** 2) % p)
#     return DP[N]
#
# for _ in range(T):
#     print(parenthesis(int(stdin.readline())))

# from sys import stdin
# p = 1000000007
# T = int(stdin.readline())
#
# DP = [None, 0, 1]
# def parenthesis(N):
#     if N % 2 == 1:
#         return 0
#     else:
#         for n in range(3, N+1):
#             sum = 0
#             if n % 2 == 0:
#                 for i in range(1, n // 2 + 1):
#                     sum += (DP[i] * DP[n - i]) % p
#                 DP.append(2 * sum % p)
#             elif n % 2 == 1:
#                 DP.append(0)
#         return DP[N]
#
# for _ in range(T):
#     print(parenthesis(int(stdin.readline())))

# from sys import stdin
# p = 1000000007
# T = int(stdin.readline())
#
# DP = [None, 0, 1, 0]
# def parenthesis(N):
#     if N % 2 == 1:
#         return 0
#     else:
#         for n in range(4, N+1, 2):
#             sum = 0
#             for i in range(2, n // 2 + 1, 2):
#                 sum += (DP[i] * DP[n - i]) % p
#             DP.append(2 * sum % p)
#             DP.append(0)
#         return DP[N]
#
# for _ in range(T):
#     print(parenthesis(int(stdin.readline())))

# from sys import stdin
# p = 1000000007
# T = int(stdin.readline())
#
# C = dict()
# C[0] = 1
# C[1] = 1
# def parenthesis(N):
#     if N % 2 == 1:
#         return 0
#     else:
#         for n in range(1, N//2+1):
#             if n not in C.keys():
#                 C[n] = 0
#                 for i in range(n):
#                     C[n] += (C[i]*C[n-1-i]) % p
#                 C[n] %= p
#         return C[N/2]
#
# for _ in range(T):
#     print(parenthesis(int(stdin.readline())))

from sys import stdin
p = 1000000007
T = int(stdin.readline())

C = dict()
C[0] = 1
C[1] = 1
def parenthesis(N):
    if N % 2 == 1:
        return 0
    else:
        for n in range(1, N//2+1):
            if n not in C.keys():
                sum = 0
                if n % 2 == 1:
                    for i in range(n//2):
                        sum += (C[i]*C[n-1-i]) % p
                    C[n] = (2*sum+C[(n-1)/2]*C[(n-1)/2]) % p
                else:
                    for i in range(n//2):
                        sum += (C[i] * C[n - 1 - i]) % p
                    C[n] = (2*sum) % p
        return C[N/2]

for _ in range(T):
    print(parenthesis(int(stdin.readline())))

# from sys import stdin # 더 고민해보기
# p = 1000000007
# T = int(stdin.readline())
#
# C = dict()
# C[0] = 1
# def parenthesis(N):
#     if N % 2 == 1:
#         return 0
#     else:
#         for n in range(1, N//2+1):
#             if n not in C.keys():
#                 sum = 0
#                 for i in range(1, n):
#                     sum += (C[i]*C[n-i]) % p # ST
#                 C[n] = (sum + C[n-1]) % p # (S)
#         return C[N/2]
#
# for _ in range(T):
#     print(parenthesis(int(stdin.readline())))